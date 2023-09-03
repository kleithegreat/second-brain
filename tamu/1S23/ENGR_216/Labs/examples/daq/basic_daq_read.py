
"""
This script will take a DAQ reading from the specified channel and print the value.
"""

from lab.daq import DAQ

# Set the DAQ channel to read from
CHANNEL = 0

# Initialize
daq = DAQ()

# Take and print reading
reading = daq.read_channel(CHANNEL)
print("Channel {} reading: {} V".format(CHANNEL, reading))
