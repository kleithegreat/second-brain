import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./insert_times.csv', usecols=[0, 1, 2, 3])
grouped_data = data.groupby('Input Size').agg(['mean', 'std'])

fig, ax = plt.subplots(figsize=(10, 6))

log_x = False
log_y = False

if log_x:
    ax.set_xscale('log')
if log_y:
    ax.set_yscale('log')

for method in ['Chaining', 'Probing', 'Double Hashing']:
    ax.errorbar(grouped_data.index, grouped_data[method]['mean'], yerr=grouped_data[method]['std'], label=method, capsize=5)

ax.set_xlabel('Input Size')
ax.set_ylabel('Time (microseconds)')
ax.set_title('Insertion Time vs Input Size')
ax.legend()

# plt.tight_layout()
plt.show()
