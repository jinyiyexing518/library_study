import pandas as pd
import numpy as np


dates = pd.date_range('20200807', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
# 缺失的数据框图
print(df)

# 是否缺失
print(df.isnull())
# 至少有一个缺失，则返回True
print(np.any(df.isnull()) == True)

# 丢弃缺失数据
# 丢掉行, how='any' how='all'
print(df.dropna(axis=0, how='any'))
# 丢掉列
print(df.dropna(axis=1, how='all'))

# 填补缺失数据
print(df.fillna(value=0))






