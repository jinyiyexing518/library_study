import pandas as pd
import numpy as np


df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])

# 竖向合并
# ignore_index对行索引重新排序
res1 = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res1)

df4 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df5 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
# inner选择相同部分拼接
res2 = pd.concat([df4, df5], join='inner', ignore_index=True)
print(res2)
# 默认为outer，补充NaN
res3 = pd.concat([df4, df5], join='outer', ignore_index=True)
print(res3)

# 按列合并
res4 = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
print(res4)

# append增加数据
res5 = df1.append([df2, df3], ignore_index=True)
print(res5)

# 单独加一组数据
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
res6 = df1.append(s1, ignore_index=True)
print(res6)




