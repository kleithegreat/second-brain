
"""
This script will take some N number of readings from the DAQ and print the average.
"""

# Import
from lab.daq import DAQ

# Declare variables
CHANNEL = 0
N = 10

# Initialize DAQ
daq = DAQ()

# Define an averaging function
def get_average(channel, n):
    total = 0
    for _ in range(n):
        reading = daq.read_channel(channel)
        total += reading
    avg = reading / n
    return avg

# Run the function
average = get_average(CHANNEL, N)
print("Average on Chnl. {}: {} V".format(CHANNEL, average))
