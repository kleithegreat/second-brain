import pandas as pd

df = pd.read_csv("module5activity.txt", header=None, squeeze=True)
print(df.mean())
print(len(df))

# 145.09 to 146.44 92% confidence interval
