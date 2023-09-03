from math import sqrt, sin, cos, pi
import pandas as pd
import matplotlib.pyplot as plt

### CLEANING UP DATA

rulerData = pd.read_csv("rulerlmao.csv")
puckData = pd.read_csv("pucklmao.csv")

# removing unused columns from both dataframes
for col_name in rulerData.columns:
    if col_name not in ["frame_no", "timestamp", "size_px-darkorange", "position_px_x-darkorange", "position_px_y-darkorange", "size_px-green", "position_px_x-green", "position_px_y-green"]:
        del rulerData[col_name]

for col_name in puckData.columns:
    if col_name not in ["frame_no", "timestamp", "position_px_x-hotpink", "position_px_y-hotpink"]:
        del puckData[col_name]

puckData.dropna(subset=["position_px_y-hotpink"], inplace=True) # drops all empty rows



### RULER STUFF
def distance(row):
    return sqrt( (row["position_px_x-darkorange"] - row["position_px_x-green"])**2 + (row["position_px_y-darkorange"] - row["position_px_y-green"])**2 )
rulerData["length"] = rulerData.apply(distance, axis=1)
averageLength = rulerData["length"].mean()

print(f"Average ruler length in pixels: {averageLength}")

# conversion factor
metersPerPixel = (5.5/39.37) / averageLength
print(metersPerPixel)

# error propagation TODO: FIGURE THIS SHIT OUT


### PUCK STUFF

startTime = 7100
endTime = 8500
puckData = puckData[(puckData['timestamp'] >= startTime) & (puckData['timestamp'] <= endTime)]

puckData["time_s"] = puckData["timestamp"] / 1000

# moving averages and finite differences
period = 3
puckData["xposavg"] = puckData["position_px_x-hotpink"].rolling(window=period).mean()
puckData["yposavg"] = puckData["position_px_y-hotpink"].rolling(window=period).mean()

puckData["xvelocity"] = puckData["xposavg"].diff() * metersPerPixel / puckData["time_s"].diff()
puckData["yvelocity"] = puckData["yposavg"].diff() * metersPerPixel / puckData["time_s"].diff()

period = 3
puckData["xvelavg"] = puckData["xvelocity"].rolling(window=period).mean()
puckData["yvelavg"] = puckData["yvelocity"].rolling(window=period).mean()

puckData["xaccel"] = puckData["xvelavg"].diff() / puckData["time_s"].diff()
puckData["yaccel"] = puckData["yvelavg"].diff() / puckData["time_s"].diff()

period = 3
puckData["xaccelavg"] = puckData["xaccel"].rolling(window=period).mean()
puckData["yaccelavg"] = puckData["yaccel"].rolling(window=period).mean()

puckData.to_csv("puckDataProcessed.csv", index=False)

# plotting position vs time

plt.figure()
plt.plot(puckData["time_s"], puckData["position_px_y-hotpink"], label="y position")
plt.plot(puckData["time_s"], puckData["position_px_x-hotpink"], label="x position")
plt.title("Position (m) vs Time (s)")
plt.legend()

# plotting velocity vs time

plt.figure()
plt.plot(puckData["time_s"], puckData["yvelocity"], label="y velocity")
plt.plot(puckData["time_s"], puckData["xvelocity"], label="x velocity")
plt.title("Velocity (m/s) vs Time (s)")
plt.legend()

# plotting acceleration vs time

plt.figure()
plt.plot(puckData["time_s"], puckData["yaccel"], label="y acceleration")
plt.plot(puckData["time_s"], puckData["xaccel"], label="x acceleration")
plt.title("Acceleration (m/s^2) vs Time (s)")
plt.legend()

plt.show()

# average acceleration
a = puckData["yaccelavg"].mean()
print(f"Average acceleration: {a}")
accelSEM = puckData["yaccel"].sem()
print(f"Standard error of the mean (acceleration): {accelSEM}")

# finding g
g = a / sin(3.6 * pi / 180)
print(f"Average g: {g}")
# propagating error for g
errorSinTheta = cos(3.6 * pi/180) * 0.2 * pi/180
errorG = sqrt( ( accelSEM / a )**2 + ( errorSinTheta / sin(3.6 * pi/180) )**2 ) * g
print(f"Propagated error of g: {errorG}")

### DEBUGGING
#print(rulerData.describe())
#print(puckData.describe())
