from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt

### CLEAING UP DATA

rulerData = pd.read_csv("ruler.csv")
puckData = pd.read_csv("puck.csv")

# removing unused columns from both dataframes
for col_name in rulerData.columns:
    if col_name not in ["frame_no", "timestamp", "size_px-hotpink", "position_px_x-hotpink", "position_px_y-hotpink", "size_px-lightorange", "position_px_x-lightorange", "position_px_y-lightorange"]:
        del rulerData[col_name]

for col_name in puckData.columns:
    if col_name not in ["frame_no", "timestamp", "size_px-hotpink", "position_px_x-hotpink", "position_px_y-hotpink"]:
        del puckData[col_name]

# drop all empty rows
rulerData.dropna(subset=["size_px-hotpink"], inplace=True)
puckData.dropna(subset=["size_px-hotpink"], inplace=True)

### RULER STUFF

# array of lengths of the ruler for each frame collected
def distance(row):
    return sqrt( (row["position_px_x-hotpink"] - row["position_px_x-lightorange"])**2 + (row["position_px_y-hotpink"] - row["position_px_y-lightorange"])**2 )

rulerData["length"] = rulerData.apply(distance, axis=1)

### PUCK STUFF
puckData = puckData.drop(puckData.index[:300]) # removes still frames from puck data

# populating velocity and acceleration for both x and y components
puckData["xvelocity"] = puckData["position_px_x-hotpink"].diff() / puckData["timestamp"].diff()
puckData["yvelocity"] = puckData["position_px_y-hotpink"].diff() / puckData["timestamp"].diff()
puckData["xvelavg"] = puckData["xvelocity"].rolling(window=10).mean()
puckData["yvelavg"] = puckData["yvelocity"].rolling(window=10).mean()

puckData["xaccel"] = puckData["xvelavg"].diff() / puckData["timestamp"].diff()
puckData["yaccel"] = puckData["yvelavg"].diff() / puckData["timestamp"].diff()
puckData["xaccelavg"] = puckData["xaccel"].rolling(window=10).mean()
puckData["yaccelavg"] = puckData["yaccel"].rolling(window=10).mean()

# plotting position vs time
plt.figure()
plt.plot(puckData["timestamp"], puckData["position_px_x-hotpink"])
plt.title("dx vs t")
plt.figure()
plt.plot(puckData["timestamp"], puckData["position_px_y-hotpink"])
plt.title("dy vs t")

# plotting velocity vs time
plt.figure()
plt.plot(puckData["timestamp"], puckData["xvelavg"])
plt.title("vx vs t")
plt.figure()
plt.plot(puckData["timestamp"], puckData["yvelavg"])
plt.title("vy vs t")

# plotting acceleration vs time
plt.figure()
plt.plot(puckData["timestamp"], puckData["xaccelavg"])
plt.title("ax vs t")
plt.figure()
plt.plot(puckData["timestamp"], puckData["yaccelavg"])
plt.title("ay vs t")

plt.show()

### DEBUGGING
#print(rulerData.describe())
#print(puckData.describe())
#puckData.to_csv("puckDataProcessed.csv", index=False)


# TODO: isolate section of data where only falling and see resulting graphs?