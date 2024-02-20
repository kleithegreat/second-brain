import pandas as pd
import matplotlib.pyplot as plt

def plot_runtime_comparison(scale='linear'):
    list_df = pd.read_csv('./list.csv')
    vector_df = pd.read_csv('./vector.csv')

    list_df.columns = ['Elements', 'TimeLinkedList']
    vector_df.columns = ['Elements', 'TimeVector']
    merged_df = pd.merge(list_df, vector_df, on='Elements')

    plt.figure(figsize=(10, 6))
    plt.plot(merged_df['Elements'], merged_df['TimeLinkedList'], label='Linked List', marker='o')
    plt.plot(merged_df['Elements'], merged_df['TimeVector'], label='Vector', marker='s')
    plt.xlabel('Number of Elements')
    plt.ylabel('Runtime (μs)')
    title = 'Elements Pushed vs Runtime (' + scale.capitalize() + ' Scale)'
    plt.title(title)
    plt.legend()
    plt.grid(True)

    if scale == 'log':
        plt.xscale('log')
        plt.yscale('log')
    elif scale == 'linear':
        plt.xscale('linear')
        plt.yscale('linear')
    else:
        raise ValueError("scale must be 'linear' or 'log'")

    plt.show()

plot_runtime_comparison('linear')
plot_runtime_comparison('log')
