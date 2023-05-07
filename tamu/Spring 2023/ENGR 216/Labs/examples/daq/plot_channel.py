
"""
Script to plot to the live voltage readings on a DAQ channel.
Channel can be specified as a command line argument with -c.
For example:
    python3 plot_channel -c 2
or
    python3 plot_channel --channel 2
would plot channel 2.
If no channel specified, script will plot channel 0.
"""

import matplotlib.pyplot as plt
from argparse import ArgumentParser
from time import time
from sys import stdin
from select import select
from lab.daq import DAQ

# Get the channel to read from
ap = ArgumentParser()
ap.add_argument('-c','--channel', nargs='+', type=int, default=[0])
args = ap.parse_args()
channel = args.channel

# DAQ and plot setup
daq = DAQ()
plt.ion()
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

# Initialize variables
x_data = []
y_data = {c : [] for c in channel}
start_time = time()

print("Plotting channel {} readings. \n Press 'Enter' to end script".format(channel))
while True:
    # Take a new readings
    x_data.append(time() - start_time)
    for c in channel:
        y_data[c].append(daq.read_channel(c))
    # Plot data
    plt.cla()
    for c in channel:
        plt.plot(x_data, y_data[c], label='Chnl. '+str(c))
    plt.legend()
    plt.title("DAQ Channel {}".format(channel))
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.pause(0.01)
    plt.draw()
    # Listen for an 'Enter' press to exit
    if stdin in select([stdin], [], [], 0)[0]:
        print("Exiting...")
        break
# Remove plot
plt.close()
