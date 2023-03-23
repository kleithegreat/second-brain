import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

puck_mass = (28, 0.5)  # mass in grams, uncertainty in grams
puck_colors = ("darkorange", "green")

# Sorted from smallest angle to largest angle
file_names = ("acute3.csv", "acute2.csv", "acute1.csv", "90.csv", "obtuse3.csv", "obtuse2.csv", "obtuse1.csv", "180.csv")

def clean_data(df: pd.DataFrame, time_range: int) -> pd.DataFrame:
    """
    Takes raw data, removes irrelevant columns, isolates rows where timestamp within timestamp +/- time_range in milliseconds

    Args:
        df (pd.DataFrame): DataFrame to clean
        time_range (int): range in milliseconds before and after collision

    Returns:
        pd.DataFrame: Cleaned DataFrame
    """

    cleaned = df

    # Removing irrelevant columns
    columns = ("frame_no", "timestamp", 
               f"rx-{puck_colors[0]}", f"ry-{puck_colors[0]}", 
               f"rx-{puck_colors[1]}", f"ry-{puck_colors[1]}", 
               f"vx-{puck_colors[0]}", f"vy-{puck_colors[0]}", 
               f"vx-{puck_colors[1]}", f"vy-{puck_colors[1]}")
    for col_name in cleaned:
        if col_name not in columns:
            del cleaned[col_name]

    # Removing irrelevant rows
    mask = (df["timestamp"] >= contact_timestamp(df) - time_range) & (df["timestamp"] <= contact_timestamp(df) + time_range)

    return cleaned[mask]


def contact_timestamp(df: pd.DataFrame) -> any:
    """
    Returns the timestamp where the pucks collide

    Args:
        df (pd.DataFrame): Input DataFrame

    Returns:
        any: timestamp of collision
    """
    # Compute the Euclidean distance between a and b at each timestamp
    dist = np.sqrt((df[f"rx-{puck_colors[0]}"] - df[f"rx-{puck_colors[1]}"])**2 + (df[f"ry-{puck_colors[0]}"] - df[f"ry-{puck_colors[1]}"])**2)
    # Find the index of the minimum distance
    idx_min = dist.idxmin()

    return df.loc[idx_min, 'timestamp']


def find_angle(df: pd.DataFrame, timestamp: int, degree: bool=False) -> float:
    """
    Calculates and returns the angle between the pucks before collision

    Args:
        df (pd.DataFrame): dataframe to calculate
        timestamp (int): timestamp where the pucks collide
        degree (bool): return value in degrees or radians (default radians)

    Returns:
        float: angle between pucks
    """
    df = df.loc[df['timestamp'] <= timestamp]

    avg_v_green = np.mean(df[[f"vx-{puck_colors[0]}", f"vy-{puck_colors[0]}"]], axis=0)
    avg_v_orange = np.mean(df[[f"vx-{puck_colors[1]}", f"vy-{puck_colors[1]}"]], axis=0)

    dot_product = np.dot(avg_v_green, avg_v_orange)
    mag_green = np.linalg.norm(avg_v_green)
    mag_orange = np.linalg.norm(avg_v_orange)

    theta = np.arccos(dot_product / (mag_green * mag_orange))
    theta_deg = np.degrees(theta)

    if degree:
        return theta_deg
    return theta


def find_momentum(df: pd.DataFrame, timestamp: int, before: bool) -> float:
    """
    Calculates and returns the momentum of the pucks before or after collision

    Args:
        df (pd.DataFrame): dataframe to calculate
        timestamp (int): timestamp where the pucks collide
        before (bool): calculate momentum before or after collision

    Returns:
        float: momentum of pucks in kg m/s
    """
    pass


def find_kinetic_energy(df: pd.DataFrame, timestamp: int, before: bool) -> float:
    """
    Calculates and returns the kinetic energy of the pucks before or after collision

    Args:
        df (pd.DataFrame): dataframe to calculate
        timestamp (int): timestamp where the pucks collide
        before (bool): calculate kinetic energy before or after collision

    Returns:
        float: kinetic energy of pucks in J
    """
    pass


def main():
    data = {find_angle(clean_data(pd.read_csv(i), 1000), contact_timestamp(clean_data(pd.read_csv(i), 1000)), degree=True): 
            clean_data(pd.read_csv(i), 1000) for i in file_names}

    # Plotting total momentum before and after collision for each angle (two graphs x and y)
    plt.figure()
    plt.title("Horizontal Momentum")
    degrees = [int(i) for i in list(data.keys())]  # use for all graphs
    #momentum_before = 
    #momentum_after = 

    plt.figure()
    plt.title("Vertical Momentum")

    # Plotting ratio of momentum before to momentum after collision for each angle (two graphs for x and y)
    plt.figure()
    plt.title("Ratio of Horizontal Momentum Before to After Collision")

    plt.figure()
    plt.title("Ratio of Vertical Momentum Before to After Collision")

    # Plotting kinetic energy before and after collision for each angle
    plt.figure()
    plt.title("Kinetic Energy")


    # plt.show()


if __name__ == "__main__":
    main()
