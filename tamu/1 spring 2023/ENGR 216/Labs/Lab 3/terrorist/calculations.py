import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce
from math import sqrt, sin, cos, atan


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


def find_theta(df: pd.DataFrame, kinetic=False) -> float:
    if kinetic:
        dx = abs(df["position_px_x-yellowneon"].mean() - df["position_px_x-hotpink"].mean())
        dy = abs(df["position_px_y-yellowneon"].mean() - df["position_px_y-hotpink"].mean())
    else:
        dx = abs(df["position_px_x-darkorange"].mean() - df["position_px_x-hotpink"].mean())
        dy = abs(df["position_px_y-darkorange"].mean() - df["position_px_y-hotpink"].mean())
    return atan(dy / dx)


def calculate_coefficients(df: pd.DataFrame) -> float:
    ax = df["ax-green"].mean()
    ay = df["ay-green"].mean()

    abs_a = sqrt(ax ** 2 + ay ** 2) / 100
    angle = find_theta(df.loc[df["frame_no"] == int(df["frame_no"].median())], kinetic=True)

    mu = (9.807 * sin(angle) - abs_a) / (9.807 * cos(angle))
    return mu


# Large side
kineticL = pd.read_csv("large side kinetic.csv")
clean_cols(kineticL, kinetic=True)
timeframes = [(2046.1, 3184.7), (5845.8, 6713.8), (9346, 10413.7), (13114.1, 13945.8), (16946.1, 17715.7), (20945.9, 21514), (25078, 26078), (29414.9, 30245.9), (33478.2, 34378.5)]
kineticL_calculations = pd.Series([calculate_coefficients(
    kineticL.loc[(kineticL['timestamp'] >= i[0]) & (kineticL['timestamp'] <= i[1])]) for i in timeframes])

# Small side
kineticS = pd.read_csv("small side kinetic.csv")
clean_cols(kineticS, kinetic=True)
timeframes = [(2114.3, 3046.2), (6016.8, 7014.4), (9814.4, 10818.1), (13614.5, 14747), (17115.6, 18114.4), (20778.6, 22046.6), (24978.9, 26278.7), (29414.4, 30746.5), (33314.6, 34246.7)]
kineticS_calculations = pd.Series([calculate_coefficients(
    kineticS.loc[(kineticS['timestamp'] >= i[0]) & (kineticS['timestamp'] <= i[1])]) for i in timeframes])

kinetic_coefficients = pd.DataFrame(
    {"Large Area": kineticL_calculations, "Small Area": kineticS_calculations})


print("KINETIC CALCULATIONS")
print(kinetic_coefficients)
print(f"Large mean and error: {kineticL_calculations.mean()} +/- {kineticL_calculations.sem()}")
print(f"Small mean and error: {kineticS_calculations.mean()} +/- {kineticS_calculations.sem()}")
