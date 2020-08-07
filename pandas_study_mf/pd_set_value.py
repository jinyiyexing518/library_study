import pandas as pd
import numpy as np


dates = pd.date_range('20200807', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])

# 利用三种选择数据的方式来set value
df.iloc[2, 2] = 1111
print(df)

df.loc['20200807', 'A'] = 2222
print(df)

# 筛选数据，更改数据
df.A[df.A > 12] = 0
print(df)

# 加上空的列（新的一列）
df['F'] = np.nan
print(df)

df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20200807', periods=6))
print(df)








