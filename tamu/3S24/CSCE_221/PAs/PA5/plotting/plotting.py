import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sort_data.csv')

sort_types = ['Bubble Sort', 'Heap Sort', 'Merge Sort', 'Quick Sort']

# Linear scale plot
plt.figure(figsize=(8, 6))
for sort_type in sort_types:
    plt.plot(data['n'], data[f'time ({sort_type.split()[0].lower()})'], marker='o', label=sort_type)
plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithms - Linear Scale')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('linear.png')
plt.close()

# Log scale plot
plt.figure(figsize=(8, 6))
for sort_type in sort_types:
    plt.plot(data['n'], data[f'time ({sort_type.split()[0].lower()})'], marker='o', label=sort_type)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of Elements (log scale)')
plt.ylabel('Time (seconds, log scale)')
plt.title('Sorting Algorithms - Log Scale')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('log.png')
plt.close()