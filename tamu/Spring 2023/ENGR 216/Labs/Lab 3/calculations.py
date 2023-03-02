import warnings
import pandas as pd
from functools import reduce
from math import sqrt, sin, cos, tan, atan

warnings.simplefilter(action='ignore', category=FutureWarning)


def clean_cols(df: pd.DataFrame, kinetic=False):
    if kinetic:
        relevant_cols = ["frame_no", "timestamp",
                         "position_px_x-yellowneon", "position_px_y-yellowneon",
                         "position_px_x-hotpink", "position_px_y-hotpink",
                         "position_px_x-darkorange", "position_px_y-darkorange",
                         "rx-green", "ry-green", "vx-green", "vy-green", "ax-green", "ay-green"]
    else:
        relevant_cols = ["frame_no", "timestamp",
                         "position_px_x-lightorange", "position_px_y-lightorange",
                         "position_px_x-hotpink", "position_px_y-hotpink",
                         "position_px_x-darkorange", "position_px_y-darkorange",
                         "rx-green", "ry-green", "vx-green", "vy-green", "ax-green", "ay-green"]
    for col_name in df.columns:
        if col_name not in relevant_cols:
            del df[col_name]


def preliminary(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df['vx-green'].diff() >= 0) & (df['vx-green'] >= 0)]


def clean_rows(df: pd.DataFrame, restrictions) -> pd.DataFrame:
    mask = reduce(lambda a, b: a | b,
                  [((df["timestamp"] >= start) & (df["timestamp"] <= stop)) for start, stop in restrictions])
    return df.loc[mask]


# STATIC FRICTION CALCULATIONS
def find_theta(df: pd.DataFrame, kinetic=False) -> float:
    if kinetic:
        dx = abs(df["position_px_x-yellowneon"].mean() - df["position_px_x-hotpink"].mean())
        dy = abs(df["position_px_y-yellowneon"].mean() - df["position_px_y-hotpink"].mean())
    else:
        dx = abs(df["position_px_x-darkorange"].mean() - df["position_px_x-hotpink"].mean())
        dy = abs(df["position_px_y-darkorange"].mean() - df["position_px_y-hotpink"].mean())
    return atan(dy / dx)


# Large side
staticL = pd.read_csv("large side static.csv")  # SECOND RUN
frames = []  # Frames where the block overcomes static friction, one frame per trial
staticL_calculations = pd.Series([tan(find_theta(staticL.loc[staticL["frame_no"] == i])) for i in frames])

# Small side
staticS = pd.read_csv("small side static.csv")
frames = []
staticS_calculations = pd.Series([tan(find_theta(staticS.loc[staticS["frame_no"] == i])) for i in frames])

static_coefficients = pd.DataFrame(
    {"Large Area": staticL_calculations, "Small Area": staticS_calculations}, index=range(1, 10))


# KINETIC FRICTION CALCULATION
def calculate_coefficients(df: pd.DataFrame) -> float:
    ax = df["ax-green"].mean()
    ay = df["ay-green"].mean()

    abs_a = sqrt(ax ** 2 + ay ** 2) / 100
    angle = find_theta(df.loc[df["frame_no"] == df["frame_no"].median()], kinetic=True)

    mu = (9.807 * sin(angle) - abs_a) / (9.807 * cos(angle))
    return mu


# Large side
kineticL = pd.read_csv("large side kinetic.csv")
clean_cols(kineticL, kinetic=True)
timeframes = [(1350, 2445), (5612, 6413), (9144, 9859), (13177, 13978), (17176, 17877), (20676, 21545), (24477, 25345),
              (28145, 28878), (31512, 32346)]

kineticL_calculations = pd.Series([calculate_coefficients(
    kineticL.loc[(kineticL['timestamp'] >= i[0]) & (kineticL['timestamp'] <= i[1])]) for i in timeframes])

# Small side
kineticS = pd.read_csv("small side kinetic.csv")
clean_cols(kineticS, kinetic=True)
timeframes = [(1914, 2746), (5515, 6449), (8646, 9415), (11846, 12679), (15180, 16179), (18578, 19580), (22046, 23014),
              (25778, 26947), (29451, 30779)]

kineticS_calculations = pd.Series([calculate_coefficients(
    kineticS.loc[(kineticS['timestamp'] >= i[0]) & (kineticS['timestamp'] <= i[1])]) for i in timeframes])

kinetic_coefficients = pd.DataFrame(
    {"Large Area": kineticL_calculations, "Small Area": kineticS_calculations}, index=range(1, 10))


print("STATIC CALCULATIONS")
print(static_coefficients)
print(f"Large mean and error: {staticL_calculations.mean()} +/- {staticL_calculations.sem()}")
print(f"Small mean and error: {staticS_calculations.mean()} +/- {staticS_calculations.sem()}")
print("---")
print("KINETIC CALCULATIONS")
print(kinetic_coefficients)
print(f"Large mean and error: {kineticL_calculations.mean()} +/- {kineticL_calculations.sem()}")
print(f"Small mean and error: {kineticS_calculations.mean()} +/- {kineticS_calculations.sem()}")

# TODO: find frames for static coefficient calculations
# TODO: fix NaN values for some kinetic mu calculations
