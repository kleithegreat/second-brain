import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./timing_data.csv") 

plt.figure(figsize=(10, 6))

plt.plot(df['InputSize'], df['TimeArrayDouble'], label='Array Double', marker='o')
plt.plot(df['InputSize'], df['TimeArrayLinear'], label='Array Linear', marker='o')
plt.plot(df['InputSize'], df['TimeLinkedList'], label='Linked List', marker='o')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Input Size')
plt.ylabel('Time (milliseconds)')
plt.title('Stack Implementation Performance Comparison')
plt.legend()

plt.show()
