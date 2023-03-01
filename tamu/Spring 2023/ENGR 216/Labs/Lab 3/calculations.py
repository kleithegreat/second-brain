import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce
from math import sqrt, sin, cos, tan, atan


# STATIC FRICTION CALCULATIONS
def find_theta(df: pd.DataFrame) -> tuple[float, str]:
    dx = abs(df["position_px_x-yellowneon"].mean() - df["position_px_x-hotpink"].mean())
    dy = abs(df["position_px_y-yellowneon"].mean() - df["position_px_y-hotpink"].mean())
    error = "lmao"
    return atan(dy / dx), error


# Large side
staticL = pd.read_csv("large side static take 2.csv")
frames = []  # Frames where the block overcomes static friction, one frame per trial
staticL_calculations = pd.DataFrame({"mu": [], "error": []})
for i in frames:
    mu = tan(find_theta(staticL.loc[staticL["frame_no"] == i])[0])
    error = "lmao"
    row = pd.Series({"mu": mu, "error": error})
    staticL_calculations.loc[len(staticL_calculations)] = row

# Small side
staticS = pd.read_csv("small side static.csv")
frames = []
staticS_calculations = pd.DataFrame({"mu": [], "error": []})


# KINETIC FRICTION CALCULATION
def plot_v(df: pd.DataFrame):
    plt.figure()
    plt.title("vx vs t")
    plt.plot(df["timestamp"], df["vx-green"])
    # plt.xticks(range(0, 34000, 1000))
    plt.show()


def plot_a(df: pd.DataFrame):
    plt.figure()
    plt.title("ax vs t")
    plt.plot(df["timestamp"], df["ax-green"])
    plt.show()


def clean_cols(df: pd.DataFrame, kinetic=False):
    if kinetic:
        relevant_cols = ["frame_no", "timestamp",
                        "position_px_x-yellowneon", "position_px_y-yellowneon",
                        "position_px_x-hotpink", "position_px_y-hotpink",
                        "position_px_x-darkorange", "position_px_y-darkorange",
                        "rx-green", "ry-green", "vx-green", "vy-green", "ax-green", "ay-green"]
    else:
        relevant_cols = []
    for col_name in df.columns:
        if col_name not in relevant_cols:
            del df[col_name]


def preliminary(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df['vx-green'].diff() >= 0) & (df['vx-green'] >= 0)]


def clean_rows(df: pd.DataFrame, restrictions) -> pd.DataFrame:
    mask = reduce(lambda a, b: a | b,
                  [((df["timestamp"] >= start) & (df["timestamp"] <= stop)) for start, stop in restrictions])
    return df.loc[mask]


def calculate_coefficients(df: pd.DataFrame) -> float:
    ax = df["ax-green"].mean()
    ay = df["ay-green"].mean()

    abs_a = sqrt(ax ** 2 + ay ** 2) / 100
    angle = find_theta(df.loc[df["frame_no"] == df["frame_no"].median()])[0]

    mu = (9.807 * sin(angle) - abs_a) / (9.807 * cos(angle))
    return mu


def calculate_coeff_error(df: pd.DataFrame) -> float:
    return 69.69


# Large side
kineticL = pd.read_csv("large side kinetic.csv")
clean_cols(kineticL, kinetic=True)
timeframes = [(1350, 2445), (5612, 6413), (9144, 9859), (13177, 13978), (17176, 17877), (20676, 21545), (24477, 25345),
              (28145, 28878), (31512, 32346)]

kineticL_calculations = pd.DataFrame({"mu": [], "error": []})
for i in timeframes:
    isolated = kineticL.loc[(kineticL['timestamp'] >= i[0]) & (kineticL['timestamp'] <= i[1])]
    row = pd.Series({"mu": calculate_coefficients(isolated), "error": calculate_coeff_error(isolated)})
    kineticL_calculations.loc[len(kineticL_calculations)] = row

# Small side
kineticS = pd.read_csv("small side kinetic.csv")
clean_cols(kineticS, kinetic=True)
timeframes = [(1914, 2746), (5515, 6449), (8646, 9415), (11846, 12679), (15180, 16179), (18578, 19580), (22046, 23014),
              (25778, 26947), (29451, 30779)]

kineticS_calculations = pd.DataFrame({"mu": [], "error": []})
for i in timeframes:
    isolated = kineticS.loc[(kineticS['timestamp'] >= i[0]) & (kineticS['timestamp'] <= i[1])]
    row = pd.Series({"mu": calculate_coefficients(isolated), "error": calculate_coeff_error(isolated)})
    kineticS_calculations.loc[len(kineticS_calculations)] = row

# TODO: fix NaN values for some kinetic mu calculations
# TODO: implement error calculation IS STANDARD ERROR ONLY NO PROPAGATION
# TODO: find relevant cols for static dataframes and update clean_cols function
