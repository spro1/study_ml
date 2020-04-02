import matplotlib.pyplot as plt

import pandas as pd


df = pd.read_csv("corona_day_date.csv", index_col='Country', header=0)
"""print(df)
df.plot()
print(df.index)
print(df.columns)
print(df.values)"""

df1 = df.transpose()
df1.plot()
print(df1)

plt.ylim(0, 250000)
plt.show()
