import socket
import struct
import atexit
import time
import numpy as np
import cv2

import time
import functools
import logging
import os
import threading
import copy
from smbus2 import SMBus

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

from ctypes import *
PWM_CONTROL_PROGRAM = "/home/deepracer/pwm_ctrl.so"
pwm_ctrl = CDLL(PWM_CONTROL_PROGRAM)

SERVER_IP = '128.194.50.58'
PORT = 65432
INT_BYTE_LIMIT = 4

# Calibration values
SERVO_MAX = 1700000
SERVO_MID = 1500000
SERVO_MIN = 1200000
MOTOR_MID = 1230000
MOTOR_MAX = MOTOR_MID + 80000
MOTOR_MIN = 1170000

POLARITY_SERVO_VAL = 1
POLARITY_MOTOR_VAL = -1
SERVO_PERIOD = 20000000


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        diff = round(time.time() - start_time, 3)
        logging.debug(f"{func.__name__} time: {str(diff)}")
        return result
    return wrapper


@log
def get_image(camera):
    if camera is None:
        return np.array([[0, 1], [2, 3]])
    rval, image = camera.read()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    scale_percent = 50 # percent of original size
    height = int(image.shape[0] * scale_percent / 100)
    width = int(image.shape[1] * scale_percent / 100)
    image = cv2.resize(image, (width, height), interpolation = cv2.INTER_AREA)

    image = cv2.imencode('.jpg', image)[1]
    return image

@log
def send_image(conn, image):
    image = np.array(image).tobytes()
    size = len(image)
    size = size.to_bytes(INT_BYTE_LIMIT, 'big')
    conn.sendall(size)
    conn.sendall(image)


@log
def send_battery(conn, batt_lvl):
    packed = struct.pack("!f", batt_lvl)
    conn.sendall(packed)


@log
def recv_action(conn):
    steering = struct.unpack("!f", conn.recv(INT_BYTE_LIMIT))[0]
    throttle = struct.unpack("!f", conn.recv(INT_BYTE_LIMIT))[0]

    return steering, throttle


@log
def compute_pwm_value(action, polarity, minv, midv, maxv):
    action = np.clip(action, -1.0, 1.0)
    adjVal = action * polarity
    if adjVal < 0:
        ret_val = midv + adjVal * (midv - minv)
    elif adjVal > 0:
        ret_val = midv + adjVal * (maxv - midv)
    else:
        ret_val = midv
    return int(ret_val)


@log
def set_motor(action):
    #pwmv = compute_pwm_value(action, POLARITY_MOTOR_VAL, MOTOR_MIN, MOTOR_MID, MOTOR_MAX)
    #duty = "/sys/class/pwm/pwmchip0/pwm0/duty_cycle"
    pwm_ctrl.writePWM(0, int(action))


@log
def set_steering(action):
    pwmv = compute_pwm_value(action, POLARITY_SERVO_VAL, SERVO_MIN, SERVO_MID, SERVO_MAX)
    #duty = "/sys/class/pwm/pwmchip0/pwm1/duty_cycle"
    pwm_ctrl.writePWM(1, pwmv)


@log
def vehicle_operation(camera, conn, battery_bus):
    image = get_image(camera)
    send_image(conn, image)
    print('batt', battery_bus.read_byte_data(0x3f, 0x03))
    send_battery(conn, float(battery_bus.read_byte_data(0x3f, 0x03)))
    steering, throttle = recv_action(conn)
    logging.info('Recvd steer: ' + str(round(steering, 3)) + ' throt: ' + str(round(throttle, 3)))
    set_steering(steering)
    set_motor(throttle)
    time.sleep(1/20)
    

def stop_vehicle():
    pwm_ctrl.writePWM(0, 0)


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
    

class AsyncCamera():
    def __init__(self):
        self.camera = cv2.VideoCapture()
        self.camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.camera.set(cv2.CAP_PROP_FPS, 30.0)
        self.camera.open(0, apiPreference=cv2.CAP_V4L2)

        self.lock = threading.Lock()
        self.status = 0
        self.frame = None

        time.sleep(5)   # Give camera time to open

        self.camera_thread = StoppableThread(target=self.update, args=())
        self.camera_thread.daemon = True
        self.camera_thread.start()

    def update(self):
        while True:
            self.lock.acquire()
            self.status, self.frame = self.camera.read()
            self.lock.release()
            time.sleep(1/20)    # Frame rate is 30

    def read(self):
        self.lock.acquire()
        frame = copy.copy(self.frame)
        status = copy.copy(self.status)
        self.lock.release()
        return status, frame
    
    def release(self):
        self.camera_thread.stop()
        self.camera_thread.join()
        self.camera.release()


@log
def main(args=None):
    atexit.register(stop_vehicle)
    battery_bus = SMBus(4)
    while (True):
        conn = None
        camera = None
        try:
            print('Waiting for connection to server')
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            while True:
                try:
                    conn.connect((SERVER_IP, PORT))
                    break
                except socket.error as err:
                    logging.debug('Connection attempted: ' + str(err))
                    time.sleep(1)

            print('Starting camera')
            camera = AsyncCamera()

            print('Ready')
            while True:
                vehicle_operation(camera, conn, battery_bus)
        except Exception as e:
            print(e)
            
            if conn is not None: conn.close()
            if camera is not None: camera.release()
            conn, camera = None, None


if __name__ == '__main__':
    main()
