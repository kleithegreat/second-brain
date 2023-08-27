# Script version

# Imports
from lab.mystery_voltage.get_mystery_voltage import MysteryDAQ
from time import time, sleep

# Initialize
mystery_voltage = MysteryDAQ()

# Script parameters
CHANNEL = 0  # DAQ channel to read from
N = 500  # Number of samples to take
DELAY = 0.01  # Seconds to pause between readings
FILENAME = "mystery_output.csv"  # Name for output file

# Takes N readings from the specified channel, along with time information
x_values = []
y_values = []
start = time()
print("Taking {} readings from Channel {}...".format(N, CHANNEL))
for _ in range(N):
    x = time()
    y = mystery_voltage.read_channel(CHANNEL)
    x_values.append(x)
    y_values.append(y)
    sleep(DELAY)
end = time()

# Calculate rate
rate = N / (end - start)
print("Data collection complete. Sample rate: {}".format(rate))

# Turn absolute time into elapsed time
x_values = [x - start for x in x_values]

# Writes a csv of the x and y values.
header1 = "Reading from Channel {} \n".format(CHANNEL)
header2 = "Time (s), Voltage (V) \n"
# Add something with the Channel here
with open(FILENAME, "w") as file:
    file.write(header1)
    file.write(header2)
    for entry in zip(x_values, y_values):
        line = [str(value) for value in entry]
        line = ",".join(line)
        line += "\n"
        file.write(line)
print("Values written to {}".format(FILENAME))
