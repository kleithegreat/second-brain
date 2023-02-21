from math import sqrt, sin, pi
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
    if col_name not in ["frame_no", "timestamp", "position_px_y-hotpink"]:
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
period = 1
puckData["yposavg"] = puckData["position_px_y-hotpink"].rolling(window=period).mean()

puckData["yvelocity"] = puckData["yposavg"].diff() * metersPerPixel / puckData["time_s"].diff()

period = 4
puckData["yvelavg"] = puckData["yvelocity"].rolling(window=period).mean()

puckData["yaccel"] = puckData["yvelavg"].diff() / puckData["time_s"].diff()

period = 2
puckData["yaccelavg"] = puckData["yaccel"].rolling(window=period).mean()

puckData.to_csv("puckDataProcessed.csv", index=False)

# plotting position vs time

plt.figure()
plt.plot(puckData["time_s"], puckData["yposavg"])
plt.plot(puckData["time_s"], puckData["position_px_y-hotpink"])
plt.title("dy vs t")

# plotting velocity vs time

plt.figure()
plt.plot(puckData["time_s"], puckData["yvelavg"])
plt.plot(puckData["time_s"], puckData["yvelocity"])
plt.title("vy vs t")

# plotting acceleration vs time

plt.figure()
plt.plot(puckData["time_s"], puckData["yaccelavg"])
plt.plot(puckData["time_s"], puckData["yaccel"])
plt.title("ay vs t")

plt.show()

# average acceleration
a = puckData["yaccelavg"].mean()
print(f"Average acceleration: {a}")

# finding g
g = puckData["yaccelavg"].mean() / sin(3.6 * pi / 180)
print(f"Average g: {g}")

### DEBUGGING
#print(rulerData.describe())
#print(puckData.describe())
