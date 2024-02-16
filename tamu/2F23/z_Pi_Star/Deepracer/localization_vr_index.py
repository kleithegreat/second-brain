import numpy as np
import math
import atexit
from concurrent.futures.thread import ThreadPoolExecutor

from websockets.sync.client import connect

from shapely.geometry import Point, Polygon
from shapely import affinity
from centerline.geometry import Centerline


def euler_from_quaternion(x, y, z, w):
    """
    Convert a quaternion into euler angles (roll, pitch, yaw)
    roll is rotation around x in degrees (counterclockwise)
    pitch is rotation around y in degrees (counterclockwise)
    yaw is rotation around z in degrees (counterclockwise)
    """
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll_x = math.atan2(t0, t1)

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t3, t4)

    return roll_x*180/math.pi, pitch_y*180/math.pi, yaw_z*180/math.pi # in degrees


class ValveIndex:

    def __init__(self):
        self.map_root = '/home/jault/projects/model_car/tmp/'
        coords = [(-0.773517, 5.649135),
                  (0.014783, 3.349087),
                  (-3.538337, 2.165315),
                  (-4.350867, 4.483304)]
        self.center_coord = (-2.04532, 4.013338)

        # Map is reloaded with offsets from original recording
        offset_x = coords[0][0] - (0.024254)
        offset_y = coords[0][1] - (-1.776745)
        self.bounds_map_calib = [(0.024254, -1.776745), (0.58907, 0.523119), (4.273964, -0.46625),
                            (3.576584, -2.787911)]  # DONT CHANGE

        print('Connecting to VR sensor...')
        self.vr_sensor = connect("ws://localhost:8080/ws")
        self.keep_going = True

        def keep_alive():
            while self.keep_going:
                self.vr_sensor.recv()

        self.keep_alive_fn = keep_alive
        self.pool = ThreadPoolExecutor(max_workers=5)
        self.keep_thr = self.pool.submit(self.keep_alive_fn)
        atexit.register(self.vr_sensor.close)

        track_outer = self.load_map(self.map_root + 'trackouter.log', offset_x, offset_y)
        track_inner1 = self.load_map(self.map_root + 'track_inner1.log', offset_x, offset_y)
        track_inner2 = self.load_map(self.map_root + 'track_inner2.log', offset_x, offset_y)

        self.bounds_map = Polygon(coords)
        self.track = Polygon(track_outer, holes=[track_inner1, track_inner2])
        self.track = self.fix_map_rotation(self.track, coords, offset_x, offset_y)
        attributes = {"id": 1, "name": "track", "valid": True}
        self.centerline = Centerline(self.track, **attributes).geometry

        def stop_going():
            self.keep_going = False

        atexit.register(stop_going)

        self.x, self.y, self.roll, self.pitch, self.yaw = -1., -1., -1., -1., -1.
        self.step = -1

    def get_reward(self, state):
        return self.reward_inside_track(state)

    def get_pose(self, step):
        if step == self.step:
            return self.x, self.y, self.roll, self.pitch, self.yaw
        self.keep_going = False
        self.keep_thr.result()
        while True:
            message = self.vr_sensor.recv()
            # If statement to grab specific lines received from the websocket (small filter)
            if ' KN0 POSE ' in message:  # KNO POSE is used to grab coordinates
                break
        data = message.split(' ')
        data2 = [float(data[each]) for each in range(3, 10) if data[each]]
        x, y, z, *other = data2
        a, b, c, d, *other = other
        roll, pitch, yaw = euler_from_quaternion(a, b, c, d)

        self.keep_going = True
        self.keep_thr = self.pool.submit(self.keep_alive_fn)
        self.x, self.y, self.roll, self.pitch, self.yaw = x, y, roll, pitch, yaw
        self.step = step
        return x, y, roll, pitch, yaw

    def reset_policy(self, step):
        x, y, roll, pitch, yaw = self.get_pose(step)
        roll = roll % 360
        newX = x - self.center_coord[0]
        newY = y - self.center_coord[1]
        angle = -(math.degrees(math.atan2(newY, newX)) + 90) % 360

        max_throttle = 1.0
        if angle - 90 < roll < angle + 90:
            if not (angle - 20 < roll < angle + 20):
                if roll > angle:
                    return 1., max_throttle
                else:
                    return -1., max_throttle
            else:
                return 0., max_throttle
        else:
            roll = roll % 180
            if not (angle - 10 < roll < angle + 10):
                if roll < angle:
                    return 1., -max_throttle
                else:
                    return -1. -max_throttle
            else:
                return 0., -max_throttle

    def in_boundary(self, step):
        x, y, _, _, _ = self.get_pose(step)
        current_xy = Point(x, y)
        return current_xy.within(self.bounds_map)

    def in_track(self, step):
        x, y, _, _, _ = self.get_pose(step)
        current_xy = Point(x, y)
        return current_xy.within(self.track)

    def centerline_distance(self, step):
        x, y, _, _, _ = self.get_pose(step)
        current_xy = Point(x, y)
        return current_xy.distance(self.centerline) * self.find_orientation_from_centerline(current_xy, self.track)

    def reward_point_reaching_distance(self, state):
        x, y, _, _, _ = self.get_pose(state[0])
        dist = np.sqrt((self.center_coord[0] - x) ** 2 + (self.center_coord[1] - y) ** 2)
        return 1 - (dist)

    def reward_point_at_centerline(self, state):
        x, y, _, _, _ = self.get_pose(state[0])
        throttle = state[2]
        current_xy = Point(x, y)

        dist = current_xy.distance(self.centerline)
        if current_xy.within(self.track):
            return 1 - (dist * 2)
        else:
            if -dist > -1: return -dist
            return -.99

    def reward_inside_track(self, state):
        x, y, _, _, _ = self.get_pose(state[0])
        current_xy = Point(x, y)

        if current_xy.within(self.track):
            return 0
        return -1

    def load_map(self, filename, offset_x, offset_y):
        track = []
        track_coords = open(filename, 'r')

        for coord in track_coords:
            t = coord.split(',')
            track.append((float(t[0]) + offset_x, float(t[1]) + offset_y))

        track_coords.close()
        return track

    def fix_map_rotation(self, track, bounds_map, offset_x, offset_y, error_threshold=1):
        coords = [(np.round(coord[0] + offset_x, 5), np.round(coord[1] + offset_y, 5)) for coord in self.bounds_map_calib]
        bounds_map_calib = Polygon(coords)
        low_percent_error = 100
        rotation_degree = 0

        # Find best rotation angle
        for x in range(361):
            coords_calib = list(affinity.rotate(bounds_map_calib, x, bounds_map[0]).exterior.coords)

            x_percent_error = np.abs(((coords_calib[2][0] - bounds_map[2][0]) / bounds_map[2][0]))
            y_percent_error = np.abs(((coords_calib[2][1] - bounds_map[2][1]) / bounds_map[2][1]))

            if (x_percent_error + y_percent_error) / 2 < low_percent_error:
                low_percent_error = (x_percent_error + y_percent_error) / 2
                rotation_degree = x

        if low_percent_error > error_threshold:
            print('Warning: Track Rotation is: ', np.round(low_percent_error * 100, 5), '%', sep='')
        else:
            print('Track Percent Error: ', np.round(low_percent_error * 100, 5), '%', sep='')
        return affinity.rotate(track, rotation_degree, bounds_map[0])

    def find_orientation_from_centerline(self, position, track):
        in_inner_blue = True
        if position.distance(Polygon(track.interiors[0].coords)) > position.distance(
                Polygon(track.interiors[1].coords)):
            in_inner_blue = False

        if in_inner_blue:
            if position.distance(track.exterior) < position.distance(track.interiors[0]):
                sign = 1
            else:
                sign = -1
        else:
            if position.distance(track.exterior) < position.distance(track.interiors[1]):
                sign = -1
            else:
                sign = 1

        return sign
