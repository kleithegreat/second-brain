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

### PUCK STUFF
startTime = 9600
endTime = 10900
puckData = puckData[(puckData['timestamp'] >= startTime) & (puckData['timestamp'] <= endTime)]

puckData.to_csv("puckDataProcessed.csv", index=False)
# moving averages and finite differences
period = 16

#puckData["xposavg"] = puckData["position_px_x-hotpink"].rolling(window=period).mean()
puckData["yposavg"] = puckData["position_px_y-hotpink"].rolling(window=period).mean()

#puckData["xvelocity"] = puckData["xposavg"].diff() / puckData["timestamp"].diff()
puckData["yvelocity"] = puckData["yposavg"].diff() / puckData["timestamp"].diff()

period = 10
#puckData["xvelavg"] = puckData["xvelocity"].rolling(window=period).mean()
puckData["yvelavg"] = puckData["yvelocity"].rolling(window=period).mean()

#puckData["xaccel"] = puckData["xvelavg"].diff() / puckData["timestamp"].diff()
puckData["yaccel"] = puckData["yvelavg"].diff() / puckData["timestamp"].diff()

period = 5
#puckData["xaccelavg"] = puckData["xaccel"].rolling(window=period).mean()
puckData["yaccelavg"] = puckData["yaccel"].rolling(window=period).mean()

# plotting position vs time
#plt.figure()
#plt.plot(puckData["timestamp"], puckData["position_px_x-hotpink"])
#plt.title("dx vs t")
plt.figure()
plt.plot(puckData["timestamp"], puckData["yposavg"])
plt.plot(puckData["timestamp"], puckData["position_px_y-hotpink"])
plt.title("dy vs t")

# plotting velocity vs time
#plt.figure()
#plt.plot(puckData["timestamp"], puckData["xvelavg"])
#plt.title("vx vs t")
plt.figure()
plt.plot(puckData["timestamp"], puckData["yvelavg"])
plt.plot(puckData["timestamp"], puckData["yvelocity"])
plt.title("vy vs t")

# plotting acceleration vs time
#plt.figure()
#plt.plot(puckData["timestamp"], puckData["xaccelavg"])
#plt.title("ax vs t")
plt.figure()
plt.plot(puckData["timestamp"], puckData["yaccelavg"])
plt.plot(puckData["timestamp"], puckData["yaccel"])
plt.title("ay vs t")

plt.show()

### DEBUGGING
#print(rulerData.describe())
#print(puckData.describe())
