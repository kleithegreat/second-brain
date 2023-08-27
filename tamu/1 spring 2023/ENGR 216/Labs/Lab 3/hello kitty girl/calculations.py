import pandas as pd
from functools import reduce
from math import sqrt, sin, cos, tan, atan


def clean_cols(df: pd.DataFrame):
    relevant_cols = ["frame_no", "timestamp",
                        "position_px_x-green", "position_px_y-green",
                        "position_px_x-hotpink", "position_px_y-hotpink",
                        "position_px_x-darkorange", "position_px_y-darkorange",
                        "rx-yellowneon", "ry-yellowneon", "vx-yellowneon", "vy-yellowneon", "ax-yellowneon", "ay-yellowneon"]
    for col_name in df.columns:
        if col_name not in relevant_cols:
            del df[col_name]


def preliminary(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df['vx-yellowneon'].diff() >= 0) & (df['vx-yellowneon'] >= 0)]


def clean_rows(df: pd.DataFrame, restrictions) -> pd.DataFrame:
    mask = reduce(lambda a, b: a | b,
                  [((df["timestamp"] >= start) & (df["timestamp"] <= stop)) for start, stop in restrictions])
    return df.loc[mask]


# STATIC FRICTION CALCULATIONS
def find_theta(df: pd.DataFrame) -> float:
    dx = abs(df["position_px_x-green"].mean() - df["position_px_x-hotpink"].mean())
    dy = abs(df["position_px_y-green"].mean() - df["position_px_y-hotpink"].mean())

    return atan(dy / dx)


# Large side
staticL = pd.read_csv("large side static.csv")
frames = [606, 1096, 1492, 1945, 3126, 3639, 4155, 4574, 5151]
staticL_calculations = pd.Series([tan(find_theta(staticL.loc[staticL["frame_no"] == i])) for i in frames])

# Small side
staticS = pd.read_csv("small side static.csv")
# frames = [149, 397, 561, 892, 1198, 1586, 2052, 2289, 2663]
frames = [97, 318, 502, 754, 1046, 1384, 1866, 2187, 2532]
staticS_calculations = pd.Series([tan(find_theta(staticS.loc[staticS["frame_no"] == i])) for i in frames])

static_coefficients = pd.DataFrame(
    {"Large Area": staticL_calculations, "Small Area": staticS_calculations})


# KINETIC FRICTION CALCULATION
def calculate_coefficients(df: pd.DataFrame) -> float:
    ax = df["ax-yellowneon"].mean()
    ay = df["ay-yellowneon"].mean()

    abs_a = sqrt(ax ** 2 + ay ** 2) / 100
    angle = find_theta(df.loc[df["frame_no"] == int(df["frame_no"].median())])

    mu = (9.807 * sin(angle) - abs_a) / (9.807 * cos(angle))
    return mu


# Large side
kineticL = pd.read_csv("large side kinetic.csv")
clean_cols(kineticL)
timeframes = [(2375.4, 4343.2), (9446.4, 11576.4), (16375.4, 18780), (35639.5, 37544.3), (48146.5, 51980.3),
              (57740.3, 61008.3), (66276.1, 69139.9), (76075.7, 78714.6), (87507.9, 90008.2)]

kineticL_calculations = pd.Series([calculate_coefficients(
    kineticL.loc[(kineticL['timestamp'] >= i[0]) & (kineticL['timestamp'] <= i[1])]) for i in timeframes])

# Small side
kineticS = pd.read_csv("small side kinetic.csv")
clean_cols(kineticS)
timeframes = [(2677.6, 3740.8), (8440.3, 9576.8), (15916, 17608.8), (23509.1, 26351.8), (32276.6, 34714.8),
              (40973.5, 43042.3), (81473.1, 81473.1), (91312.2, 92074.4), (101041.3, 103673.3)]

kineticS_calculations = pd.Series([calculate_coefficients(
    kineticS.loc[(kineticS['timestamp'] >= i[0]) & (kineticS['timestamp'] <= i[1])]) for i in timeframes])

kinetic_coefficients = pd.DataFrame(
    {"Large Area": kineticL_calculations, "Small Area": kineticS_calculations})


print("STATIC CALCULATIONS")
print(static_coefficients)
print(f"Large mean and error: {staticL_calculations.mean()} +/- {staticL_calculations.sem()}")
print(f"Small mean and error: {staticS_calculations.mean()} +/- {staticS_calculations.sem()}")
print("---")
print("KINETIC CALCULATIONS")
print(kinetic_coefficients)
print(f"Large mean and error: {kineticL_calculations.mean()} +/- {kineticL_calculations.sem()}")
print(f"Small mean and error: {kineticS_calculations.mean()} +/- {kineticS_calculations.sem()}")
