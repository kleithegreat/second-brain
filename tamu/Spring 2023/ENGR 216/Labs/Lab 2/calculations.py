from math import sqrt
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
    if col_name not in ["frame_no", "timestamp", "position_px_x-hotpink", "position_px_y-hotpink"]:
        del puckData[col_name]

# drop all empty rows
rulerData.dropna(subset=["position_px_x-hotpink"], inplace=True)
puckData.dropna(subset=["position_px_y-hotpink"], inplace=True)

### RULER STUFF

# array of lengths of the ruler for each frame collected
def distance(row):
    return sqrt( (row["position_px_x-hotpink"] - row["position_px_x-lightorange"])**2 + (row["position_px_y-hotpink"] - row["position_px_y-lightorange"])**2 )

rulerData["length"] = rulerData.apply(distance, axis=1)
averageLength = rulerData["length"].mean()
print(f"Average ruler length in pixels: {averageLength}")

# to meters
metersPerPixel = 0.5 / averageLength

### PUCK STUFF
startTime = 9600
endTime = 10900
puckData = puckData[(puckData['timestamp'] >= startTime) & (puckData['timestamp'] <= endTime)]

puckData["time_s"] = puckData["timestamp"] / 1000

puckData.to_csv("puckDataProcessed.csv", index=False)

# moving averages and finite differences
period = 16
puckData["yposavg"] = puckData["position_px_y-hotpink"].rolling(window=period).mean()

puckData["yvelocity"] = puckData["yposavg"].diff() * metersPerPixel / puckData["time_s"].diff()

period = 10
puckData["yvelavg"] = puckData["yvelocity"].rolling(window=period).mean()

puckData["yaccel"] = puckData["yvelavg"].diff() / puckData["time_s"].diff()

period = 5
puckData["yaccelavg"] = puckData["yaccel"].rolling(window=period).mean()

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

### DEBUGGING
#print(rulerData.describe())
#print(puckData.describe())
