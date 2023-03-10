### Imports ###
import matplotlib.pyplot as plt
import numpy as np
from lab.scanning import Scanner
from lab.cnc import VProbe

### Script variables ###
OUTPUT_NAME = "scan_output"
KWARGS = {
    "pattern": "straight",
    "scan_algorithm": "continuous",
    "step_size": 25.4,
    "x_steps": 5,
    "y_steps": 5,
    "center": (400, 400, 0),
    "scan_velocity": 100,
    "step_up": True,
}


def plot_potential(data):
    """
    Plots the readings as a matplotlib figure.
    Plot is a heatmap.
    """
    # Plot setup
    plt.ion()
    fig, ax = plt.subplots()
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    # Make heatmap
    c = ax.pcolormesh(data, cmap="RdBu_r")
    ax.invert_yaxis()
    ax.set_title("Potential scan")
    ax.set_xlabel("CNC Y-axis (steps)")
    ax.set_ylabel("CNC X-axis (steps)")
    fig.colorbar(c, ax=ax)
    plt.pause(0.1)
    plt.draw()
    # Save image
    input("Press 'Enter' to save plot and quit...")
    print("Saving heatmap to {}".format(OUTPUT_NAME + ".png"))
    fig.savefig(OUTPUT_NAME + ".png")
    # Cleanup
    plt.clf()
    plt.close()


if __name__ == "__main__":
    v = VProbe()
    scanner = Scanner(v.get_voltage, **KWARGS)
    data = scanner.run_scan()
    data = np.transpose(data)
    with open(OUTPUT_NAME + ".csv", "w") as f:
        np.savetxt(f, data, delimiter=",")
    plot_potential(data)
