import threading
from inputs import get_gamepad
import math
from model_car_env import ModelCar
import time
import cv2
import csv

import torch
from supervised import VisionModel, device, eval_transformer, num_stacked_images, stack_transformer
from model_car_env import ModelCar
from collections import deque
import numpy as np


class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def read(self): # return the buttons/triggers that you care about in this methode
        x = self.RightJoystickX / XboxController.MAX_JOY_VAL # normalize between -1 and 1
        y = self.LeftJoystickY / XboxController.MAX_JOY_VAL # normalize between -1 and 1
        return [-x, -y]

    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state 
                # elif event.code == 'ABS_X':
                #     self.LeftJoystickX = event.state
                # elif event.code == 'ABS_RY':
                #     self.RightJoystickY = event.state
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state
                # elif event.code == 'ABS_Z':
                #     self.LeftTrigger = event.state
                # elif event.code == 'ABS_RZ':
                #     self.RightTrigger = event.state
                # elif event.code == 'BTN_TL':
                #     self.LeftBumper = event.state
                # elif event.code == 'BTN_TR':
                #     self.RightBumper = event.state
                # elif event.code == 'BTN_SOUTH':
                #     self.A = event.state
                # elif event.code == 'BTN_NORTH':
                #     self.Y = event.state #previously switched with X
                # elif event.code == 'BTN_WEST':
                #     self.X = event.state #previously switched with Y
                # elif event.code == 'BTN_EAST':
                #     self.B = event.state
                # elif event.code == 'BTN_THUMBL':
                #     self.LeftThumb = event.state
                # elif event.code == 'BTN_THUMBR':
                #     self.RightThumb = event.state
                # elif event.code == 'BTN_SELECT':
                #     self.Back = event.state
                # elif event.code == 'BTN_START':
                #     self.Start = event.state
                # elif event.code == 'BTN_TRIGGER_HAPPY1':
                #     self.LeftDPad = event.state
                # elif event.code == 'BTN_TRIGGER_HAPPY2':
                #     self.RightDPad = event.state
                # elif event.code == 'BTN_TRIGGER_HAPPY3':
                #     self.UpDPad = event.state
                # elif event.code == 'BTN_TRIGGER_HAPPY4':
                #     self.DownDPad = event.state


def write_image_to_disk(img, index, steering, throttle, pose, time):
    x, y, roll, pitch, yaw = pose
    cv2.imwrite('./data/image_' + str(index) + '.jpg', img)
    with open('labels.csv', 'a+', newline='\n') as csvfile:
        fieldnames = ['image', 'steering', 'throttle', 'x', 'y', 'roll', 'pitch', 'yaw', 'time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'image': 'image_' + str(index) + '.jpg', 'steering': steering, 'throttle': throttle,
                         'x': x, 'y': y, 'roll': roll, 'pitch': pitch, 'yaw': yaw, 'time': time})


ctrl = XboxController()

model = torch.load('model_995.pth')
model.to(device)
model.eval()

env = ModelCar()
obs = env.reset()

images = deque(maxlen=num_stacked_images)
for i in range(num_stacked_images-1): images.append(stack_transformer(obs))

motor_stop = 1280000
motor = 1280000

i = 0
while True:
    images.append(stack_transformer(obs))
    image = np.stack(images, axis=0)
    image = torch.Tensor(image).to(device)
    image = eval_transformer(image)

    #speed = model(torch.unsqueeze(image, 0))

    steering, throttle = ctrl.read()
    if throttle > 0.1:
        throttle = 1.
    else:
        throttle = 0.

    # if throttle == 1.:
    #     if speed < 22.0:
    #         motor = max(motor-500, motor_stop-60000)
    #     elif 22 > speed > 25:
    #         pass
    #     else:
    #         motor = min(motor+500, motor_stop)
    # else:
    #     motor = motor_stop

    obs, pose = env.do_action([steering, throttle])

    act_time = time.time()
    t1 = threading.Thread(target=write_image_to_disk, args=(obs, i, steering, throttle, pose, act_time))
    t1.start()
    print(i, steering, throttle)
    i += 1
