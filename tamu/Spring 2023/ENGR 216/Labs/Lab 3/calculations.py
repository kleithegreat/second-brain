import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce
from math import sqrt, sin, cos, tan, atan


# STATIC FRICTION CALCULATIONS
def find_theta(row) -> float:
    dx = abs(row["position_px_x-yellowneon"] - row["position_px_x-hotpink"])
    dy = abs(row["position_px_y-yellowneon"] - row["position_px_y-hotpink"])
    return atan(dy / dx)


# Large side
staticL = pd.read_csv("large side static take 2.csv")
frames = []
coefficientsLarge = []
for i in frames:
    coefficientsLarge.append(tan(find_theta(staticL.loc[staticL["frame_no"] == i])))

# Small side
staticS = pd.read_csv("small side static.csv")
frames = []
coefficientsSmall = []
for i in frames:
    coefficientsSmall.append(tan(find_theta(staticS.loc[staticS["frame_no"] == i])))


# KINETIC FRICTION CALCULATION
def plot_v(df):
    plt.figure()
    plt.title("vx vs t")
    plt.plot(df["timestamp"], df["vx-green"])
    # plt.xticks(range(0, 34000, 1000))
    plt.show()


def plot_a(df):
    plt.figure()
    plt.title("ax vs t")
    plt.plot(df["timestamp"], df["ax-green"])
    plt.show()
    
    
def clean_cols(df):
    relevant_cols = ["frame_no", "timestamp",
                     "position_px_x-yellowneon", "position_px_y-yellowneon",
                     "position_px_x-hotpink", "position_px_y-hotpink",
                     "position_px_x-darkorange", "position_px_y-darkorange",
                     "rx-green", "ry-green", "vx-green", "vy-green", "ax-green", "ay-green"]
    for col_name in df.columns:
        if col_name not in relevant_cols:
            del df[col_name]


def preliminary(df) -> pd.DataFrame:
    return df[(df['vx-green'].diff() >= 0) & (df['vx-green'] >= 0)]


def clean_rows(df, restrictions) -> pd.DataFrame:
    mask = reduce(lambda a, b: a | b,
                  [((df["timestamp"] >= start) & (df["timestamp"] <= stop)) for start, stop in restrictions])
    return df.loc[mask]


def find_mu(accel, theta) -> float:
    return (9.807 * sin(theta) - accel) / (9.807 * cos(theta))


# TODO: IMPLEMENTING ONE COEFFICIENT CALCULATION FOR EACH TRIAL:
# Iterate over timeframes array
# for each timeframe: run calculations for mu, use dataframe indexing 


# Large side
kineticL = pd.read_csv("large side kinetic.csv")
clean_cols(kineticL)
timeframes = [(1350, 2445), (5612, 6413), (9144, 9859), (13177, 13978), (17176, 17877), (20676, 21545), (24477, 25345),
              (28145, 28878), (31512, 32346)]
kineticL = clean_rows(kineticL, timeframes)

ax = kineticL["ax-green"].mean()
ay = kineticL["ay-green"].mean()

abs_a = sqrt(ax ** 2 + ay ** 2) / 100
angle = find_theta(kineticL.loc[kineticL["frame_no"] == 44])

mu = find_mu(abs_a, angle)

print(f"Large side average acceleration: {abs_a} ms^-2")
print(f"Large side coefficient: {mu}")

# Small side
kineticS = pd.read_csv("small side kinetic.csv")
clean_cols(kineticS)
timeframes = [(1914, 2746), (5515, 6449), (8646, 9415), (11846, 12679), (15180, 16179), (18578, 19580), (22046, 23014),
              (25778, 26947), (29451, 30779)]
kineticS = clean_rows(kineticS, timeframes)

ax = kineticS["ax-green"].mean()
ay = kineticS["ay-green"].mean()

abs_a = sqrt(ax ** 2 + ay ** 2) / 100
angle = find_theta(kineticL.loc[kineticL["frame_no"] == 44])

mu = find_mu(abs_a, angle)

print(f"Small side average acceleration: {sqrt(ax ** 2 + ay ** 2) / 100} ms^-2")
print(f"Small side coefficient: {mu}")
