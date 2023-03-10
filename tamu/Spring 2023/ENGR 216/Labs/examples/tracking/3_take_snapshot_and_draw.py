
'''
Demo of using TrackingCamera to draw text, circle and arrow on frame
display the frame, and save it as an image
'''

## import camera
from lab.tracking import TrackingCamera

def run_camera():
    ## create camera with configuration, and init with resources
    # will throw exception for errors (such as broken camera or non-existing input/config files, ...)
    camera_kwargs = {
        'input_source': 0,                    # camera id (0, 1,...) or input video file name (default is camera 0)
        'mode': 'recording',                  # optional, the camera mode [recording, tracking (default), motion, calibration]
        'camera_settings': (1920, 1080, 30),  # optional (width, height, fps), (1920, 1080, 30) by default
        'crop': True,                         # optional, if True (default) frame is cropped to near square, otherwise use full resolution
        'flip_method': 2                      # 0=no rotation, 2= rotate 180 degrees, 4=horizontal flip, 6=vertical-flip
    }

    with TrackingCamera(**camera_kwargs) as camera:
        ## read camera
        # return frame number, timestamp (in ms), and the frame
        # if the read failed (due to hardware or driver issues, ...), return values are None
        frame_no, frame_ts, frame = camera.read_frame()

        ## drawing on frame (text, circle, arrow)
        camera.draw_text(frame,               # frame to draw on, do not change
                         text="Test drawing", # the text you want to draw, modify if you like
                         position=(100, 200), # (x,y) position of the bottom-left of the text block
                         color=(0, 0, 255),   # color of the text, specified using the BGR scheme
                         fontScale=5,         # selects the font size
                         thickness=5)         # selects the thicnkess of the text font
        camera.draw_circle(frame,
                           center=(600, 300), radius=100,
                           color=(255, 0, 0),
                           thickness=10)
        camera.draw_arrow(frame,
                          start=(50, 600), end=(750, 600),
                          color=(0, 255, 0),
                          thickness=5)

        ## save frame to file
        # to filename if it's given or to a filename composed with datetime and frame_no
        # ignore (and print warning) if frame is invalid
        camera.write_frame_to_image(frame_no, frame, filename='example_3.png')

        ## display frame (statically) in window
        # stop by pressing `q` or `Ctrl-C` in command line
        # ignore (and print warning) if frame is invalid
        camera.display_static_frame(frame_no, frame, window="snapshot")

        # following codes will not execute until display is done


## run in command line
if __name__ == "__main__":
    run_camera()
