import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read the CSV file
data = pd.read_csv('insert_trials.csv')

# Calculate the mean and confidence interval for each input size and hash table type
grouped_data = data.groupby(['Input Size', 'Trial']).mean().reset_index()
mean_data = grouped_data.groupby('Input Size').mean()
std_data = grouped_data.groupby('Input Size').std()
ci_data = 1.96 * std_data / np.sqrt(10)  # Assuming 10 trials per input size

# Create a line plot with error bars
# plt.figure(figsize=(10, 6))
plt.errorbar(mean_data.index, mean_data['Chaining'], yerr=ci_data['Chaining'], capsize=3, label='Chaining')
plt.errorbar(mean_data.index, mean_data['Probing'], yerr=ci_data['Probing'], capsize=3, label='Probing')
plt.errorbar(mean_data.index, mean_data['Double Hashing'], yerr=ci_data['Double Hashing'], capsize=3, label='Double Hashing')

# Set a logarithmic scale for the x-axis
# plt.xscale('log')

# Add labels and title
plt.xlabel('Input Size')
plt.ylabel('Insertion Time (ms)')
plt.title('Insertion Time Comparison')

# Add legend
plt.legend()

# Display the plot
plt.show()