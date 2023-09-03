### Imports ###
from math import log
from sys import stdin
from select import select
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from lab.scanning import Vector, vectorize
from lab.cnc import MAG
from lab.scanning import Scanner

### Variables ###
OUTPUT_NAME = "scan_output"
KWARGS = {
    "pattern": "snake",
    "scan_algorithm": "continuous",
    "step_size": 25.4,
    "x_steps": 5,
    "y_steps": 5,
    "z_steps": 1,
    "center": (400, 400, 0),
    "scan_velocity": 100,
}


### Utility functions ###


def write_data(data, f):
    """
    Writes data out to a csv title OUTPUT_NAME
    """
    header = ",".join(
        [
            "x position (step #)",
            "y position (step #)",
            "z position (step #)",
            "B_x (microT)",
            "B_z (microT)",
            "B_z (microT)",
        ]
    )
    f.write(header + "\n")
    for index, vec in np.ndenumerate(data):
        if data.ndim == 2:
            x, y = index
            z = 0
        elif data.ndim == 3:
            x, y, z = index
        v_x, v_y, v_z = vec.values
        values = [str(a) for a in [x, y, z, v_x, v_y, v_z]]
        line = ",".join(values)
        f.write(line + "\n")


def apply_log_scale(data):
    """
    Applies a log scale to the x and y data..
    """
    # Ensure all greater than 1
    data = np.vectorize(lambda x: x + x / x.magnitude)(data)
    # Apply log
    scale = np.vectorize(lambda x: log(x.magnitude) / x.magnitude)(data)
    data = data * scale
    return data


### Define plotting functions ###


def make_2d_plot(data, filename):
    """
    Produces a matplotlib figure from the data.
    2D quiver with colorbar included.
    """
    if data.ndim != 2:
        raise ValueError("Data has wrong dimensionality")
    # Correct CNC axes to plot axes
    data = np.transpose(data)
    # Initial plot setup
    fig, ax = plt.subplots()
    # Configure color mapping
    magnitudes = np.vectorize(lambda v: v.magnitude)(data).flatten()
    norm = Normalize()
    norm.autoscale(magnitudes)
    colormap = cm.copper
    sm = cm.ScalarMappable(cmap=colormap, norm=norm)
    sm.set_array([])
    # Get x and y data
    data = np.vectorize(lambda v: Vector(v.x, v.y))(data)
    data = apply_log_scale(data)
    x_data = np.vectorize(lambda v: -v.x)(data)
    y_data = np.vectorize(lambda v: v.y)(data)
    # Make plot
    q = ax.quiver(
        y_data, x_data, pivot="mid", scale_units="xy", color=colormap(norm(magnitudes))
    )
    ax.set_xlabel("CNC Y-axis (steps)")
    ax.set_ylabel("CNC X-axis (steps)")
    ax.set_title("Magnetic Field (vectors log scaled, color scale in actual μT)")
    ax.invert_yaxis()
    # Create colorbar
    cbar = plt.colorbar(sm)
    cbar.set_label("Field strength (microT)", rotation=90)
    display_2d_plot(fig, filename)


def display_2d_plot(fig, filename, fullscreen=False):
    """
    Displays vector plot on screen.
    Also saves an image of the plot.
    """
    if fullscreen:
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
    plt.pause(0.1)
    plt.draw()
    # Save image
    input("Press 'Enter' to save image and quit...")
    print("Saving field plot to {}.png".format(filename))
    fig.savefig(filename + ".png")
    # Cleanup
    plt.clf()
    plt.close()


def make_3d_plot(data, filename):
    """
    Plots the vector field as a matplotlib figure.
    Rotating 3D quiver plot.
    """
    if data.ndim != 3:
        raise ValueError("Data has wrong dimensionality")
    # Unpack
    x_data = np.vectorize(lambda v: v.x)(data)
    y_data = np.vectorize(lambda v: v.y)(data)
    z_data = np.vectorize(lambda v: v.z)(data)
    # Get positions
    y_pos, z_pos, x_pos = np.meshgrid(
        np.arange(data.shape[1]), np.arange(data.shape[0]), np.arange(data.shape[2])
    )
    # Plot setup
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    ax.set_xlabel("CNC X-axis")
    ax.set_ylabel("CNC Y-axis")
    ax.set_zlabel("CNC Z-axis")
    # Plot
    q = ax.quiver(
        x_pos,
        y_pos,
        z_pos,
        x_data,
        y_data,
        z_data,
        length=0.4,
        normalize=True,
        pivot="middle",
    )
    display_3d_plot(fig, filename)


def display_3d_plot(fig, filename, fullscreen=False):
    """
    Rotates the 3D model.
    Also saves an image of the model.
    """
    # Set fullscreen
    if fullscreen:
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
    # Save
    print("Saving field plot to {}._3D.png".format(filename))
    fig.savefig(OUTPUT_NAME + "_3D.png")
    # Display plot and rotate
    angle = 0
    print("Press 'Enter' to quit display...")
    while True:
        ax.view_init(30, angle)
        plt.draw()
        plt.pause(0.01)
        angle = (angle + 1) % 360
        if stdin in select([stdin], [], [], 0)[0]:
            print("Exiting...")
            break


### Run the script ###

if __name__ == "__main__":
    m = MAG()
    measurement_function = vectorize(m.get_field)
    scanner = Scanner(measurement_function, **KWARGS)
    data = scanner.run_scan()
    with open(OUTPUT_NAME + ".csv", "w") as f:
        write_data(data, f)
    if scanner.z_steps == 1:
        make_2d_plot(data, OUTPUT_NAME)
    elif scanner.z_steps > 1:
        make_3d_plot(data, OUTPUT_NAME)
