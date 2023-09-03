import pandas as pd
import numpy as np
from scipy.signal import find_peaks
import uncertainties as unc
import matplotlib.pyplot as plt

files = (("data/green_spring_400g.csv", unc.ufloat(0.4, 0.003)), 
         ("data/red_spring_400g.csv", unc.ufloat(0.4, 0.003)), 
         ("data/white_spring_300g.csv", unc.ufloat(0.3, 0.003)))  # (filename, mass and uncertainty in kg)

cols = ("frame_no", "timestamp", "size_px-green", "position_px_x-green", "position_px_y-green")


def clean_data(df: pd.DataFrame, cols: tuple) -> pd.DataFrame:
    """
    Removes irrelevant columns and imcomplete rows from the dataframe.

    Args:
        df (pd.DataFrame): dataframe to be cleaned

    Returns:
        pd.DataFrame: cleaned dataframe
    """
    cleaned = df.copy()
    cleaned = cleaned.loc[:, cols]
    cleaned = cleaned.dropna(subset="size_px-green")

    return cleaned


def isolate(df: pd.DataFrame, start: int, end: int) -> pd.DataFrame:
    """
    Isolates a section of the dataframe between the start and end times.

    Args:
        df (pd.DataFrame): dataframe to be isolated
        start (int): start time
        end (int): end time

    Returns:
        pd.DataFrame: isolated dataframe
    """
    isolated = df.copy()
    isolated = isolated.loc[(isolated["timestamp"] >= start) & (isolated["timestamp"] <= end)]

    return isolated


def find_period(df: pd.DataFrame) -> unc.ufloat:
    """
    Finds the period of the oscillation in the dataframe.

    Args:
        df (pd.DataFrame): dataframe to be analysed

    Returns:
        unc.ufloat: period of oscillation
    """
    heights = df["position_px_y-green"].values
    times = df["timestamp"].values

    peak_indices, _ = find_peaks(heights)
    periods = np.diff(times[peak_indices])
    avg_period = np.mean(periods)
    period_unc = np.std(periods) / np.sqrt(len(periods))
    
    return unc.ufloat(avg_period, period_unc)


def find_k(T: unc.ufloat, m: unc.ufloat) -> unc.ufloat:
    """
    Finds the spring constant of the oscillation in the dataframe.

    Args:
        T (unc.ufloat): period of oscillation
        m (unc.ufloat): mass of the oscillating object

    Returns:
        unc.ufloat: spring constant
    """
    return (4 * np.pi ** 2 * m) / T ** 2


def main():
    green = isolate(clean_data(pd.read_csv(files[0][0]), cols), 5053, 15817)
    red = isolate(clean_data(pd.read_csv(files[1][0]), cols), 5611, 23444)
    white = clean_data(pd.read_csv(files[2][0]), cols)

    green_k = find_k(find_period(green), files[0][1])
    red_k = find_k(find_period(red), files[1][1])
    white_k = find_k(find_period(white), files[2][1])

    print(f"Green spring: {green_k}")
    print(f"Red spring: {red_k}")
    print(f"White spring: {white_k}")

    plt.figure()
    plt.plot(green["timestamp"], green["position_px_y-green"], color="green", label="Green spring")
    plt.title("Height vs time for green spring")
    plt.xlabel("Time (milliseconds)")
    plt.ylabel("Height (pixels)")
    plt.savefig("figures/green_height_vs_time.png")

    plt.figure()
    plt.plot(red["timestamp"], red["position_px_y-green"], color="red", label="Red spring")
    plt.title("Height vs time for red spring")
    plt.xlabel("Time (milliseconds)")
    plt.ylabel("Height (pixels)")
    plt.savefig("figures/red_height_vs_time.png")

    plt.figure()
    plt.plot(white["timestamp"], white["position_px_y-green"], color="black", label="White spring")
    plt.title("Height vs time for white spring")
    plt.xlabel("Time (milliseconds)")
    plt.ylabel("Height (pixels)")
    plt.savefig("figures/white_height_vs_time.png")


if __name__ == "__main__":
    main()
