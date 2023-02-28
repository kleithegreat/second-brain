import pandas as pd
from functools import reduce
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# STATIC FRICTION CALCULATIONS
staticL = pd.read_csv("large side static take 2.csv")
staticS = pd.read_csv("small side static.csv")

# function to find angle of ramp for a given dataframe row


# KINETIC FRICTION CALCULATION

# Large side
kineticL = pd.read_csv("squid game girl.csv")

plt.figure()
plt.title("raw data v")
plt.plot(kineticL["timestamp"], kineticL["vx-yellowneon"])
plt.show()

# removing useless columns
for col_name in kineticL.columns:
    if col_name not in ["frame_no", "timestamp", "position_px_x-darkorange", "position_px_y-darkorange", "position_px_x-hotpink", "position_px_y-hotpink","position_px_x-lightorange", "position_px_y-lightorange", "rx-yellowneon", "ry-yellowneon", "vx-yellowneon", "vy-yellowneon", "ax-yellowneon", "ay-yellowneon"]:
        del kineticL[col_name]

# selected timeframes of only sliding
timeframesL = [(5500, 6500), (9500, 10500), (13200, 14100), (16800, 17700), (21000, 21500), (25000, 25500), (29000, 29700), (32100, 33000), (35200, 36000)]
# removing everything outside of timeframes
mask = reduce(lambda a, b: a | b, [((kineticL['timestamp'] >= start) & (kineticL['timestamp'] <= stop)) for start, stop in timeframesL])
kineticL = kineticL.loc[mask]

print(kineticL["ax-yellowneon"].mean())
print(kineticL["ay-yellowneon"].mean())

kineticL.to_csv("lmao.csv", index=False)
