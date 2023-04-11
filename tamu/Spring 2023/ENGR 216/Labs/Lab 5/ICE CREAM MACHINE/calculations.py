import pandas as pd
import numpy as np
import uncertainties as unc
import matplotlib.pyplot as plt

moment_L = (0.00097, 0.00007)  # moment of inertia, uncertainty both in kg m^2
moment_mass = (0.00000132, 0.00000005)
mass = 0.02  # kg
colors = ("lightorange", "hotpink", "yellowneon")  # center, shape, mass


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes unnecessary columns and converts centimeters to meters.

    Args:
        df (pd.DataFrame): dataframe to clean

    Returns:
        pd.DataFrame: cleaned dataframe
    """
    cols = ["frame_no", "timestamp", 
            f"rx-{colors[0]}", f"ry-{colors[0]}", 
            f"rx-{colors[1]}", f"ry-{colors[1]}",
            f"rx-{colors[2]}", f"ry-{colors[2]}"]
    
    # Make a copy of the DataFrame and select only the desired columns
    df_cleaned = df[cols].copy()

    # Convert position data from cm to m
    for color in colors:
        df_cleaned[f"rx-{color}"] /= 100
        df_cleaned[f"ry-{color}"] /= 100
    
    return df_cleaned


def recenter(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recenter the data to the center of the rotating object.

    Args:
        df (pd.DataFrame): dataframe to recenter

    Returns:
        pd.DataFrame: new re-centered dataframe
    """

    # Get the center of the rotating object
    center_x = df[f"rx-{colors[0]}"].median()
    center_y = df[f"ry-{colors[0]}"].median()

    # Recenter the data in a new dataframe
    df_recentered = df.copy()
    df_recentered[f"rx-{colors[0]}"] -= center_x
    df_recentered[f"ry-{colors[0]}"] -= center_y
    df_recentered[f"rx-{colors[1]}"] -= center_x
    df_recentered[f"ry-{colors[1]}"] -= center_y
    df_recentered[f"rx-{colors[2]}"] -= center_x
    df_recentered[f"ry-{colors[2]}"] -= center_y

    return df_recentered


def make_polar(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a new dataframe with polar coordinates and angular velocity for the moving point on the shape and the mass.

    Args:
        df (pd.DataFrame): dataframe to convert

    Returns:
        pd.DataFrame: new dataframe with polar coordinates and angular velocity for the moving point on the shape and
        the mass
    """

    df_polar = df.copy()
    # create new columns for polar coordinates and angular velocity
    df_polar["r-shape"] = np.sqrt((df[f"rx-{colors[1]}"] ** 2) + (df[f"ry-{colors[1]}"] ** 2))
    df_polar["theta-shape"] = np.arctan2(df[f"ry-{colors[1]}"], df[f"rx-{colors[1]}"])
    df_polar["r-mass"] = np.sqrt((df[f"rx-{colors[2]}"] ** 2) + (df[f"ry-{colors[2]}"] ** 2))
    df_polar["theta-mass"] = np.arctan2(df[f"ry-{colors[2]}"], df[f"rx-{colors[2]}"])

    df_polar["omega-shape"] = df_polar["theta-shape"].diff() / df_polar["timestamp"].diff() * 1000
    df_polar["omega-mass"] = df_polar["theta-mass"].diff() / df_polar["timestamp"].diff() * 1000

    return df_polar


def find_contact(df: pd.DataFrame) -> float:
    """
    Finds the time when the mass first makes contact with the shape.

    Args:
        df (pd.DataFrame): dataframe to search

    Returns:
        float: time of contact
    """
    index = df["omega-mass"].first_valid_index()
    timestamp = df.loc[index, "timestamp"]
    return timestamp


def main():
    # Plotting angular momentum of the L-Shape

    lshape = make_polar(recenter(clean_data(pd.read_csv("data/lshape.csv"))))  # Read in data and clean it
    # Remove NaNs and negative angular velocities
    lshape = lshape[(lshape["omega-shape"].notna()) & (lshape["omega-shape"] > 0) & 
                    ((lshape["omega-mass"].isna()) | (lshape["omega-mass"] >= 0))]

    lshape["omega-mass"] = lshape["omega-mass"].fillna(0)  # Fill NaNs with 0
    lshape = lshape[(lshape["timestamp"] >= 1000)]  # Remove first second of data
    lshape["timestamp"] = lshape["timestamp"] * 1000  # Convert to s from ms
    
    # Calculate angular momentum of the shape   
    lshape["shape-L"] = moment_L[0] * lshape["omega-shape"]  
    # Calculate angular momentum of the mass using parallel axis theorem
    lshape["mass-L"] = (moment_mass[0] + mass * lshape["r-mass"].median()**2) * lshape["omega-mass"]
    # Calculate total angular momentum
    lshape["total-L"] = lshape["mass-L"] + lshape["shape-L"]  

    plt.figure()
    plt.scatter(lshape["timestamp"], lshape["shape-L"], label="L-Shape")
    plt.scatter(lshape["timestamp"], lshape["mass-L"], label="Mass")
    plt.scatter(lshape["timestamp"], lshape["total-L"], label="Total")
    plt.xlabel("Time (s)")
    plt.ylabel("Angular Momentum (kg m^2/s)")
    plt.legend()
    plt.savefig("figures/angular_momentum.png")
    
    # Calculating the moment of inertia of the circular object
    circle = make_polar(recenter(clean_data(pd.read_csv("data/circle.csv"))))
    circle = circle[(circle["omega-shape"].notna()) & (circle["omega-shape"] > 0) & 
                    ((circle["omega-mass"].isna()) | (circle["omega-mass"] >= 0))]
    circle = circle.iloc[10:-10]  # Remove first and last ten rows

    Im = unc.ufloat(moment_mass[0], moment_mass[1])
    m = unc.ufloat(mass, 0)

    d = unc.ufloat(circle["r-mass"].median(), circle["r-mass"].sem())
    wi = unc.ufloat(circle[circle["timestamp"] <= find_contact(circle)]["omega-shape"].mean(), 
                    circle[circle["timestamp"] <= find_contact(circle)]["omega-shape"].sem())
    wf = unc.ufloat(circle[circle["timestamp"] >= find_contact(circle)]["omega-shape"].mean(), 
                    circle[circle["timestamp"] >= find_contact(circle)]["omega-shape"].sem())

    moment_circle = (Im + m * d**2) * wf / (wi - wf)

    # Calculating the moment of inertia of the pentagon object
    pentagon = make_polar(recenter(clean_data(pd.read_csv("data/pentagon.csv"))))
    pentagon = pentagon[(pentagon["omega-shape"].notna()) & (pentagon["omega-shape"] > 0) & 
                        ((pentagon["omega-mass"].isna()) | (pentagon["omega-mass"] >= 0))]
    pentagon = pentagon.iloc[10:-10]  # Remove first and last ten rows

    d = unc.ufloat(pentagon["r-mass"].median(), pentagon["r-mass"].sem())
    wi = unc.ufloat(pentagon[pentagon["timestamp"] <= find_contact(pentagon)]["omega-shape"].mean(), 
                    pentagon[pentagon["timestamp"] <= find_contact(pentagon)]["omega-shape"].sem())
    wf = unc.ufloat(pentagon[pentagon["timestamp"] >= find_contact(pentagon)]["omega-shape"].mean(), 
                    pentagon[pentagon["timestamp"] >= find_contact(pentagon)]["omega-shape"].sem())

    moment_pentagon = (Im + m * d**2) * wf / (wi - wf)

    print(f"Circle moment of inertia: {moment_circle} kg m^2")
    print(f"Pentagon moment of inertia: {moment_pentagon} kg m^2")


if __name__ == '__main__':
    main()
