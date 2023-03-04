import pandas as pd
import matplotlib.pyplot as plt

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

kineticL = pd.read_csv("large side kinetic.csv")
kineticS = pd.read_csv("small side kinetic.csv")
clean_cols(kineticL)
clean_cols(kineticS)
kineticL = preliminary(kineticL)
kineticS = preliminary(kineticS)
kineticL.to_csv("kineticL.csv", index=False)
kineticS.to_csv("kineticS.csv", index=False)

staticL = pd.read_csv("large side static.csv")
staticS = pd.read_csv("small side static.csv")

plt.plot(staticS["frame_no"], staticS["vx-yellowneon"])
plt.show()
