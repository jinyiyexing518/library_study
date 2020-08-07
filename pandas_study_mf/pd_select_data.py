import pandas as pd
import numpy as np


dates = pd.date_range('20200807', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
# 打印出来的结果一样
print(df['A'], df.A)
print(df[0: 3], df['20200807': '20200809'])

# df.loc标签定位
print(df.loc['20200807'])
print(df.loc[:, ['A', 'B']])
print(df.loc['20200807', ['A', 'B']])

# df.iloc索引定位
print(df.iloc[3])
print(df.iloc[1:3, 1:3])
print(df.iloc[[1, 3, 5], 1:3])

print(df.ix[:3, ['A', 'C']])

# 筛选数据
print(df[df.A > 8])
print(df[df.A < 8])




