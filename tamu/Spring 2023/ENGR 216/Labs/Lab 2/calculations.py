from math import sqrt, sin, pi
import pandas as pd
import matplotlib.pyplot as plt

### CLEANING UP DATA

rulerData = pd.read_csv("ruler.csv")
puckData = pd.read_csv("puck.csv")

# removing unused columns from both dataframes
for col_name in rulerData.columns:
    if col_name not in ["frame_no", "timestamp", "size_px-hotpink", "position_px_x-hotpink", "position_px_y-hotpink", "size_px-lightorange", "position_px_x-lightorange", "position_px_y-lightorange"]:
        del rulerData[col_name]

for col_name in puckData.columns:
    if col_name not in ["frame_no", "timestamp", "position_px_y-hotpink"]:
        del puckData[col_name]

puckData.dropna(subset=["position_px_y-hotpink"], inplace=True) # drops all empty rows



### RULER STUFF
def distance(row):
    return sqrt( (row["position_px_x-hotpink"] - row["position_px_x-lightorange"])**2 + (row["position_px_y-hotpink"] - row["position_px_y-lightorange"])**2 )
rulerData["length"] = rulerData.apply(distance, axis=1)
averageLength = rulerData["length"].mean()
avgLenSEM = rulerData["length"].sem()

print(f"Average ruler length in pixels: {averageLength}")
print(f"Standard error of the mean (ruler length in pixels): {avgLenSEM}")

# conversion factor
metersPerPixel = 0.5 / averageLength
print(f"Meters per pixel: {metersPerPixel}")

# error propagation


### PUCK STUFF

startTime = 9600
endTime = 10900
puckData = puckData[(puckData['timestamp'] >= startTime) & (puckData['timestamp'] <= endTime)]

puckData["time_s"] = puckData["timestamp"] / 1000

# moving averages and finite differences
period = 3
puckData["yposavg"] = puckData["position_px_y-hotpink"].rolling(window=period).mean()

puckData["yvelocity"] = puckData["yposavg"].diff() * metersPerPixel / puckData["time_s"].diff()

period = 4
puckData["yvelavg"] = puckData["yvelocity"].rolling(window=period).mean()

puckData["yaccel"] = puckData["yvelavg"].diff() / puckData["time_s"].diff()

period = 3
puckData["yaccelavg"] = puckData["yaccel"].rolling(window=period).mean()

puckData.to_csv("puckDataProcessed.csv", index=False)

# plotting position vs time

plt.figure()
plt.plot(puckData["time_s"], puckData["yposavg"], label="Smoothed position (period = 3)")
plt.plot(puckData["time_s"], puckData["position_px_y-hotpink"], label="Raw position")
plt.title("Position (m) vs Time (s)")
plt.xlabel("Position (m)")
plt.ylabel("Time (s)")
plt.legend()

# plotting velocity vs time

plt.figure()
plt.plot(puckData["time_s"], puckData["yvelavg"], label="Smoothed velocity (period = 4)")
plt.plot(puckData["time_s"], puckData["yvelocity"], label="Raw Velocity")
plt.title("Velocity (m/s) vs Time (s)")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Time (s)")
plt.legend()

# plotting acceleration vs time

plt.figure()
plt.plot(puckData["time_s"], puckData["yaccelavg"], label="Smoothed acceleration (period = 3)")
plt.plot(puckData["time_s"], puckData["yaccel"], label="Raw acceleration")
plt.title("Acceleration (m/s^2) vs Time (s)")
plt.xlabel("Acceleration (m/s^2)")
plt.ylabel("Time (s)")
plt.legend()

plt.show()

# average acceleration
a = puckData["yaccelavg"].mean()
print(f"Average acceleration: {a}")
accelSEM = puckData["yaccel"].sem()
print(f"Standard error of the mean (acceleration): {accelSEM}")

# finding g
g = puckData["yaccelavg"].mean() / sin(3.6 * pi / 180)
print(f"Average g: {g}")

### DEBUGGING
#print(rulerData.describe())
#print(puckData.describe())

# TODO: make error propagation formulas in code
# ADD X COMPONENT TOO ALL GRAPHS
