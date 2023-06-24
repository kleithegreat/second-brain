
'''
Demo of using TrackingCamera class.
Tracks camera input and prints tracking data in terminal.
Data and video are saved (`example_4.csv` and `example_4.mp4`).
'''

from lab.tracking import TrackingCamera

def run_camera():
    
    # Set TrackingCamera arguments. 
    camera_kwargs = {
        'input_source': 0,                    # camera id (0, 1,...) or input video file name (default is camera 0)
        'output_video': 'example_4.mp4',      # optional, save the output video file (`mp4` format only)
        'output_data': 'example_4.csv',       # optional, save the tracking data (to `.csv` files)
        'camera_settings': (1920, 1080, 30),  # optional (width, height, fps), (1920, 1080, 30) by default
        'tracking_config_file': 'stickers',   # optional, markers for tracking or motion
                                              #           '<name>' for builtin config or '<name>.config' for local file
        'marker_names': [],                   # optional, selected markers in tracking config (empty for all)
        'crop': True,                         # optional, if True (default) frame is cropped to near square, otherwise the full resolution is used
        'builtin_plot_mode': 'default',       # optional, 'none' for no plotting by lib
                                              #           'default' for plotting center, contour, etc, may add 'trace' for future
        'camera_distance': 100,               # approx. camera distance (in cm) to object
                                              # required for proper sticker tracking
        'flip_method': 0                      # 0=no rotation, 2= rotate 180 degrees, 4=horizontal flip, 6=vertical-flip
    }

    # Create & run TrackingCamera instance.
    with TrackingCamera(**camera_kwargs) as camera:
        while camera.is_running:

            # Read tracking data, then display and write out. 
            tracking_frame_no, tracking_frame = camera.read_track()
            camera.write_frame_to_video(tracking_frame_no, tracking_frame)
            camera.display_frame(tracking_frame_no, tracking_frame)

            # Print tracking info to the terminal.
            if tracking_frame_no is None:
                continue
            if (tracking_frame_no % 30 == 0 and tracking_frame_no > 0):
                tracking_frame_ts = camera.get_timestamp_of_frame(tracking_frame_no)
                print("Frame #{}, {:.1f}ms Stickers: ".format(tracking_frame_no, tracking_frame_ts))
                for marker_name, marker_data in camera.get_tracking_data_of_frame(tracking_frame_no):
                    y, x = marker_data["position_pixel"]
                    print("{}: ({}, {}), ".format(marker_name, y, x),end = '')
                print("")

# Run main.
if __name__ == "__main__":
    run_camera()
