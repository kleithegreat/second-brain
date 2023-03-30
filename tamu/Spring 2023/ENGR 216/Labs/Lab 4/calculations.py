import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

puck_mass = (0.028, 0.0005)  # mass and uncertainty in kg
puck_colors = ("yellowneon", "green")

# Sorted from smallest to largest angle
file_names = ("data\\acute1.csv", "data\\acute2.csv", "data\\acute3.csv", "data\\90.csv", 
              "data\\obtuse1.csv", "data\\obtuse2.csv", "data\\obtuse3.csv", "data\\180.csv")


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


def clean_data(df: pd.DataFrame, time_range: int) -> pd.DataFrame:
    """
    Takes raw data, removes irrelevant columns, isolates rows surrounding impact where velocity is constant,
    and returns a cleaned DataFrame

    Args:
        df (pd.DataFrame): DataFrame to clean
        time_range (int): range in milliseconds before and after collision

    Returns:
        pd.DataFrame: Cleaned DataFrame
    """

    # Removing irrelevant columns
    columns = ("frame_no", "timestamp", 
               f"rx-{puck_colors[0]}", f"ry-{puck_colors[0]}", 
               f"rx-{puck_colors[1]}", f"ry-{puck_colors[1]}", 
               f"vx-{puck_colors[0]}", f"vy-{puck_colors[0]}", 
               f"vx-{puck_colors[1]}", f"vy-{puck_colors[1]}",
               f"ax-{puck_colors[0]}", f"ay-{puck_colors[0]}", 
               f"ax-{puck_colors[1]}", f"ay-{puck_colors[1]}"
               )
    for col_name in df:
        if col_name not in columns:
            del df[col_name]

    # Removing extra rows
    mask = (df["timestamp"] >= contact_timestamp(df) - time_range) & (df["timestamp"] <= contact_timestamp(df) + time_range)

    # Converting cm to m
    for col_name in df:
        if f"{puck_colors[0]}" in col_name or f"{puck_colors[1]}" in col_name:
            df[col_name] = df[col_name] / 100

    return df[mask]


def find_angle(df: pd.DataFrame, timestamp: int, degree: bool = False) -> float:
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

    avg_v_1 = np.mean(df[[f"vx-{puck_colors[0]}", f"vy-{puck_colors[0]}"]], axis=0)
    avg_v_2 = np.mean(df[[f"vx-{puck_colors[1]}", f"vy-{puck_colors[1]}"]], axis=0)

    dot_product = np.dot(avg_v_1, avg_v_2)
    mag_1 = np.linalg.norm(avg_v_1)
    mag_2 = np.linalg.norm(avg_v_2)

    theta = np.arccos(dot_product / (mag_1 * mag_2))
    theta_deg = np.degrees(theta)

    if degree:
        return theta_deg
    return theta


def isolate(df: pd.DataFrame, t1: int, t2: int) -> pd.DataFrame:
    """
    Isolates a range of rows in a DataFrame

    Args:
        df (pd.DataFrame): DataFrame to isolate
        t1 (int): start timestamp
        t2 (int): end timestamp

    Returns:
        pd.DataFrame: Isolated DataFrame
    """
    mask = (df["timestamp"] >= t1) & (df["timestamp"] <= t2)
    return df[mask]
    

def find_momentum(df: pd.DataFrame, x_or_y: bool) -> tuple:
    """
    Calculates and returns the total absolute momentum and error of the pucks for a single component before collision

    Args:
        df (pd.DataFrame): dataframe to calculate
        x_or_y (bool): calculate momentum in x or y direction, true is x, false is y

    Returns:
        tuple: total momentum and error
    """
    if x_or_y:
        avg_v_1 = np.abs(np.mean(df[f"vx-{puck_colors[0]}"]))
        avg_v_2 = np.abs(np.mean(df[f"vx-{puck_colors[1]}"]))
        ev1 = df[f"vx-{puck_colors[0]}"].sem()
        ev2 = df[f"vx-{puck_colors[1]}"].sem()
    else:
        avg_v_1 = np.abs(np.mean(df[f"vy-{puck_colors[0]}"]))
        avg_v_2 = np.abs(np.mean(df[f"vy-{puck_colors[1]}"]))
        ev1 = df[f"vy-{puck_colors[0]}"].sem()
        ev2 = df[f"vy-{puck_colors[1]}"].sem()

    p1 = puck_mass[0] * avg_v_1
    p2 = puck_mass[0] * avg_v_2

    p = p1 + p2

    ep1 = p1 * (ev1 / avg_v_1)
    ep2 = p2 * (ev2 / avg_v_2)

    e = np.sqrt(ep1**2 + ep2**2)
    
    return p, e


def find_kinetic_energy(df: pd.DataFrame) -> tuple:
    """
    Calculates and returns the total kinetic energy and error of the pucks

    Args:
        df (pd.DataFrame): dataframe to calculate

    Returns:
        tuple: total kinetic energy and error
    """
    v1 = np.sqrt(df[f"vx-{puck_colors[0]}"].mean()**2 + df[f"vy-{puck_colors[0]}"].mean()**2)
    v2 = np.sqrt(df[f"vx-{puck_colors[1]}"].mean()**2 + df[f"vy-{puck_colors[1]}"].mean()**2)

    ke1 = 0.5 * puck_mass[0] * v1**2
    ke2 = 0.5 * puck_mass[0] * v2**2

    ke = ke1 + ke2
    
    # propagated error of velocity magnitude
    errorv1 = np.sqrt((df[f"vx-{puck_colors[0]}"].sem() / df[f"vx-{puck_colors[0]}"].mean())**2 + (df[f"vy-{puck_colors[0]}"].sem() / df[f"vy-{puck_colors[0]}"].mean())**2)
    errorv2 = np.sqrt((df[f"vx-{puck_colors[1]}"].sem() / df[f"vx-{puck_colors[1]}"].mean())**2 + (df[f"vy-{puck_colors[1]}"].sem() / df[f"vy-{puck_colors[1]}"].mean())**2)

    e1 = ke1 *  errorv1/ v1
    e2 = ke2 * errorv2 / v2

    e = np.sqrt(e1 ** 2 + e2 ** 2)

    return ke, e


def plot_v(data: dict, save: bool = False):
    for i in data:
        plt.figure()
        plt.plot(data[i]["timestamp"], data[i][f"vx-{puck_colors[0]}"], marker="o",label=f"vx-{puck_colors[0]}")
        plt.plot(data[i]["timestamp"], data[i][f"vx-{puck_colors[1]}"], marker="o",label=f"vx-{puck_colors[1]}")
        plt.title(f"vx-{puck_colors[0]} and vx-{puck_colors[1]} for angle {i} degrees")
        plt.legend()
        if save:
            plt.savefig(f"figures\\v\\vx-{puck_colors[0]} and vx-{puck_colors[1]} for {i} degrees.png")

        plt.figure()        
        plt.plot(data[i]["timestamp"], data[i][f"vy-{puck_colors[0]}"], marker="o",label=f"vy-{puck_colors[0]}")
        plt.plot(data[i]["timestamp"], data[i][f"vy-{puck_colors[1]}"], marker="o",label=f"vy-{puck_colors[1]}")
        plt.title(f"vy-{puck_colors[0]} and vy-{puck_colors[1]} for angle {i} degrees")
        plt.legend()
        if save:
            plt.savefig(f"figures\\v\\vy-{puck_colors[0]} and vy-{puck_colors[1]} for {i} degrees.png")
    
    plt.show()


def plot_r(data: dict, save: bool = False):
    for i in data:
        plt.figure()
        plt.plot(data[i]["timestamp"], data[i][f"rx-{puck_colors[0]}"], marker="o",label=f"rx-{puck_colors[0]}")
        plt.plot(data[i]["timestamp"], data[i][f"rx-{puck_colors[1]}"], marker="o",label=f"rx-{puck_colors[1]}")
        plt.title(f"rx-{puck_colors[0]} and rx-{puck_colors[1]} for angle {i} degrees")
        plt.legend()
        if save:
            plt.savefig(f"figures\\r\\rx-{puck_colors[0]} and rx-{puck_colors[1]} for {i} degrees.png")

        plt.figure()        
        plt.plot(data[i]["timestamp"], data[i][f"ry-{puck_colors[0]}"], marker="o",label=f"ry-{puck_colors[0]}")
        plt.plot(data[i]["timestamp"], data[i][f"ry-{puck_colors[1]}"], marker="o",label=f"ry-{puck_colors[1]}")
        plt.title(f"ry-{puck_colors[0]} and ry-{puck_colors[1]} for angle {i} degrees")
        plt.legend()
        if save:
            plt.savefig(f"figures\\r\\ry-{puck_colors[0]} and ry-{puck_colors[1]} for {i} degrees.png")
    
    plt.show()


def export_csv(data: dict, time_range: int):
    for i in data:
        clean_data(data[i], time_range).to_csv(f"processed\\{i}.csv", index=False)


def main():
    timestamps_before = [(2608.3, 2709.2), (2313.4, 2645.8), (2082.7, 2244.6), (2674.8, 2911.1), (2205.3, 2605), (3477.3, 3942), (2511.6, 2843.6), (2439.4, 2739.3)]  # Start and end timestamps for each angle before collision
    timestamps_after = [(2944.2, 3244.3), (2877.9, 3246.1), (2476.6, 2776,6), (3110.6, 3474.5), (2845.3, 3269.3), (4277.9, 4677.9), (3075.5, 3443.7), (2975.6, 3313)]  # Start and end timestamps for each angle after collision

    data = {}
    for i, v in enumerate(file_names):
        df = isolate(clean_data(pd.read_csv(v), 1000), timestamps_before[i][0], timestamps_after[i][1])
        key = f"{float(find_angle(isolate(df, timestamps_before[i][0], timestamps_before[i][1]), contact_timestamp(df), degree=True)):.2f}"
        data[key] = df

    # Momentum x before and after collision
    fig, ax = plt.subplots()

    x = data.keys()
    p0 = [find_momentum(isolate(data[v], timestamps_before[i][0], timestamps_before[i][1]), True)[0] for i, v in enumerate(x)]
    pf = [find_momentum(isolate(data[v], timestamps_after[i][0], timestamps_after[i][1]), True)[0] for i, v in enumerate(x)]
    error_p0 = [find_momentum(isolate(data[v], timestamps_before[i][0], timestamps_before[i][1]), True)[1] for i, v in enumerate(x)]
    error_pf = [find_momentum(isolate(data[v], timestamps_after[i][0], timestamps_after[i][1]), True)[1] for i, v in enumerate(x)]

    width = 0.35

    ax.set_xticks(np.arange(len(x)))
    ax.set_xticklabels(x)

    ax.bar(np.arange(len(x)), p0, width, yerr = error_p0,label = 'Momentum Before')
    ax.bar(np.arange(len(x)) + width , pf, width, yerr = error_pf, label = 'Momentum After')

    ax.set_ylabel('Momentum (kg m/s)')
    ax.set_xlabel('Angle (degrees)')
    ax.set_title('Momentum x before and after collision')
    ax.legend()

    plt.savefig(f"figures\\px.png")

    # Momentum y before and after collision
    fig, ax = plt.subplots()

    x = data.keys()
    p0 = [find_momentum(isolate(data[v], timestamps_before[i][0], timestamps_before[i][1]), False)[0] for i, v in enumerate(x)]
    pf = [find_momentum(isolate(data[v], timestamps_after[i][0], timestamps_after[i][1]), False)[0] for i, v in enumerate(x)]
    error_p0 = [find_momentum(isolate(data[v], timestamps_before[i][0], timestamps_before[i][1]), False)[1] for i, v in enumerate(x)]
    error_pf = [find_momentum(isolate(data[v], timestamps_after[i][0], timestamps_after[i][1]), False)[1] for i, v in enumerate(x)]

    width = 0.35

    ax.set_xticks(np.arange(len(x)))
    ax.set_xticklabels(x)

    ax.bar(np.arange(len(x)), p0, width, yerr = error_p0,label = 'Momentum Before')
    ax.bar(np.arange(len(x)) + width , pf, width, yerr = error_pf, label = 'Momentum After')

    ax.set_ylabel('Momentum (kg m/s)')
    ax.set_xlabel('Angle (degrees)')
    ax.set_title('Momentum y before and after collision')
    ax.legend()

    plt.savefig(f"figures\\py.png")

    # Ratio of momentum x before collision to momentum x after collision
    fig, ax = plt.subplots()

    x = data.keys()
    ratio = [find_momentum(isolate(data[v], timestamps_before[i][0], timestamps_before[i][1]), True)[0] / find_momentum(isolate(data[v], timestamps_after[i][0], timestamps_after[i][1]), True)[0] for i, v in enumerate(x)]
    error = [ratio[i] * np.sqrt((find_momentum(isolate(data[v], timestamps_before[i][0], timestamps_before[i][1]), True)[1] / find_momentum(isolate(data[v], timestamps_before[i][0], timestamps_before[i][1]), True)[0])**2 + (find_momentum(isolate(data[v], timestamps_after[i][0], timestamps_after[i][1]), True)[1] / find_momentum(isolate(data[v], timestamps_after[i][0], timestamps_after[i][1]), True)[0])**2) for i, v in enumerate(x)]

    ax.set_xticks(np.arange(len(x)))
    ax.set_xticklabels(x)

    ax.bar(np.arange(len(x)), ratio, width, yerr=error, label = 'Ratio')

    ax.set_ylabel('Ratio')
    ax.set_xlabel('Angle (degrees)')
    ax.set_title('Ratio of momentum x before collision to momentum x after collision')

    plt.savefig(f"figures\\ratio_x.png")

    # Ratio of momentum y before collision to momentum y after collision
    fig, ax = plt.subplots()

    x = data.keys()
    ratio = [find_momentum(isolate(data[v], timestamps_before[i][0], timestamps_before[i][1]), False)[0] / find_momentum(isolate(data[v], timestamps_after[i][0], timestamps_after[i][1]), False)[0] for i, v in enumerate(x)]
    error = [ratio[i] * np.sqrt((find_momentum(isolate(data[v], timestamps_before[i][0], timestamps_before[i][1]), True)[1] / find_momentum(isolate(data[v], timestamps_before[i][0], timestamps_before[i][1]), True)[0])**2 + (find_momentum(isolate(data[v], timestamps_after[i][0], timestamps_after[i][1]), True)[1] / find_momentum(isolate(data[v], timestamps_after[i][0], timestamps_after[i][1]), True)[0])**2) for i, v in enumerate(x)]

    ax.set_xticks(np.arange(len(x)))
    ax.set_xticklabels(x)

    ax.bar(np.arange(len(x)), ratio, width, yerr=error, label = 'Ratio')

    ax.set_ylabel('Ratio')
    ax.set_xlabel('Angle (degrees)')
    ax.set_title('Ratio of momentum y before collision to momentum y after collision')

    plt.savefig(f"figures\\ratio_y.png")

    # Kinetic energy before and after collision
    fig, ax = plt.subplots()

    x = data.keys()
    ke0 = [find_kinetic_energy(isolate(data[v], timestamps_before[i][0], timestamps_before[i][1]))[0] for i, v in enumerate(x)]
    kef = [find_kinetic_energy(isolate(data[v], timestamps_after[i][0], timestamps_after[i][1]))[0] for i, v in enumerate(x)]
    error_ke0 = [find_kinetic_energy(isolate(data[v], timestamps_before[i][0], timestamps_before[i][1]))[1] for i, v in enumerate(x)]
    error_kef = [find_kinetic_energy(isolate(data[v], timestamps_after[i][0], timestamps_after[i][1]))[1] for i, v in enumerate(x)]

    width = 0.35

    ax.set_xticks(np.arange(len(x)))
    ax.set_xticklabels(x)

    ax.bar(np.arange(len(x)), ke0, width, yerr = error_ke0,label = 'Kinetic Energy Before')
    ax.bar(np.arange(len(x)) + width , kef, width, yerr = error_kef, label = 'Kinetic Energy After')

    ax.set_ylabel('Kinetic Energy (J)')
    ax.set_xlabel('Angle (degrees)')
    ax.set_title('Kinetic energy before and after collision')
    ax.legend()

    plt.savefig(f"figures\\ke.png")
    

    plt.show()


if __name__ == "__main__":
    main()
