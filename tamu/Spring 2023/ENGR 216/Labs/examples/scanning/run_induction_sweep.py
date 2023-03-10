
# Import
from lab.scanning import Sweeper
from lab.daq import DAQ
import matplotlib.pyplot as plt

# Variables
center = (200, 400, 0)
sweep_length = 450
velocity = 100
channel = 0
min_sample = 2000
collect_position = False

# Initialize DAQ and plot
daq = DAQ()
plt.ion()
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

# Define how to creat a plot
def plot_data(x_data, y_data):
    plt.clf()
    plt.plot(x_data, y_data)
    plt.xlabel("Time (seconds)")
    plt.ylabel("EMF (Volts)")
    plt.pause(0.1)
    plt.draw()
    
# Create sweeper object
sweeper = Sweeper(
    measurement_function=lambda: daq.read_channel(channel),
    center=center,
    sweep_length=sweep_length,
    min_sample=min_sample,
    collect_position=collect_position
)

# Run a sweep
time_data, _, readings = sweeper.sweep(velocity)
plot_data(time_data, readings)
plt.close()
