import pandas as pd
import numpy as np


s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)

dates = pd.date_range('20200807', periods=6)
print(dates)

# DataFrame
# index为行，columns为列
df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)
# 默认0、1、2...
df1 = pd.DataFrame(np.arange(12).reshape(3, 4))
print(df1)
# 字典形式
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': np.array([3] * 4, dtype='int32'),
                    'D': pd.Series(1, index=list(range(2, 6)), dtype='float32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2, '\n', df2.dtypes, '\n', df2.index, '\n', df2.columns, '\n', df2.values)
# 计数、max、min、mean、std...等数据描述
print(df2.describe())
# 转置
print(df2.T)
# 排序
print(df2.sort_index(axis=0, ascending=False))
print(df2.sort_index(axis=1, ascending=False))
print(df2.sort_values(by='E'))




