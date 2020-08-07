import pandas as pd
import numpy as np


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
# 一个key的合并
res1 = pd.merge(left, right, on='key')
print(res1)

left2 = pd.DataFrame({'key1': ['K0', 'K0', 'K2', 'K2'],
                      'key2': ['K1', 'K1', 'K2', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K1', 'K2', 'K2', 'K1'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
# how = {'left', 'right', 'inner', 'outer'}
# inner：相同key，对于每一类型，二者数量相乘为该类型总数量
res2 = pd.merge(left2, right2, on=['key1', 'key2'], how='inner')
print(res2)

# indicator
# 显示合并的方式，left only、right only、both
# 还可以自定义名字，indicator='indicator_column'
res3 = pd.merge(left2, right2, on=['key1', 'key2'], how='outer', indicator=True)
print(res3)

# index
left3 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']},
                     index=['K0', 'K0', 'K2', 'K3'])
right3 = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']},
                      index=['K0', 'K1', 'K2', 'K3'])

res4 = pd.merge(left3, right3, left_index=True, right_index=True, how='outer')
print(res4)

# 防止overlapping问题
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})

# 加入后缀, 就可以区分了
res5 = pd.merge(boys, girls, on='k', suffixes=['_boys', '_girls'], how='outer')
print(res5)



