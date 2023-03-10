__version__ = "1.0"
"""
Basic scatter plot using matplotlib
"""

import matplotlib.pyplot as plt

# Define data to plot
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Setup plot
plt.ion()
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

# Make scatter plot
plt.scatter(x, y)
plt.title("An example scatter plot")
plt.xlabel("x axis title")
plt.ylabel("y axit title")

# Display and then close
plt.pause(0.1)
plt.draw()
input("Press 'Enter' to end...")
plt.close()
