__version__ = "1.0"
"""
This script can be used to take multiple DAQ readings while changing some independent variable.
(voltage, force, etc.)
Independent variable values are manually entered by the user. 
The script will produce a CSV containg the collected data (measurements + uncertainty).
"""

from time import time
import numpy as np
from math import sqrt
from lab.daq import DAQ
from tqdm import tqdm as progress_bar

# Variables:
N = 1000            # The number of samples to take for a single reading.
CHANNELS = [1, 2]   # A list of the channels to be read from. Can provide any number of channels.
POINTS = 3          # The number of readings that will be taken from each channel.
FILENAME = "output" # Filename used for the CSV output.

# Initialize DAQ
daq = DAQ()

def take_reading(channel, sample_size):
    """Take sample_size readings from each channel.
    Returns the average total.
    """
    # Initialize data
    data = np.zeros((sample_size))
    # Collect data
    t_start = time()
    for i in progress_bar(range(sample_size)):
        data[i] = daq.read_channel(channel)
    t_end = time()
    # Calculate rate
    print("Sample rate:", sample_size / (t_end - t_start))
    # Calc average
    avg = np.mean(data)
    err = np.std(data) / sqrt(sample_size)
    print("Chnl. {} reading: {} ± {} V".format(channel, avg, err))
    return avg, err

def get_config(x):
    """Gets the measurement setting for
    the independent variable from the user.
    """
    print("")
    while True:
        x_value = input("Enter the value for {}: ".format(x.lower()))
        try:
            x_value = float(x_value)
        except ValueError:
            print("Not a valid value...")
        else:
            return x_value

### Main ###
if __name__ == "__main__":

    # Get variable informaiton from user
    print("\n * Set independent variable *")
    VARIABLE = input("What is the independent variable?: ").rstrip()
    UNITS = input("What units are you using for {}?: ".format(VARIABLE)).rstrip()

    # Initialize output file
    with open(FILENAME + ".csv", "w") as output:
        header = ["Chnl. {0} (V), Chnl. {0} uncert. (V)".format(c) for c in CHANNELS]
        header = ["Applied {} ({})".format(VARIABLE, UNITS)] + header
        header = ",".join(header)
        output.write(header + "\n")

    # Take data
    for _ in range(POINTS):
        value = get_config(VARIABLE)
        readings = []
        for c in CHANNELS:
            reading, uncert = take_reading(c, N)
            readings.append(reading)
            readings.append(uncert)
        with open(FILENAME + ".csv", "a") as output:
            line = [value] + readings
            line = [str(entry) for entry in line]
            line = ",".join(line)
            output.write(line + "\n")

    print("\n", "Data collection complete.")
