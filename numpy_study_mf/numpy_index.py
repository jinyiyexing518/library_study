import numpy as np


a = np.arange(3, 15).reshape(3, 4)
print(a)
# 索引第二行, 第一行第一列
print(a[2], a[2:, ], a[1][1], a[1, 1])
# 打印第一行，1，2列
print(a[1, 1:3])
# 倒索引
print(a[::-1, ::-1])

# 迭代行
for row in a:
    print(row)
# 迭代列
for column in a.T:
    print(column)
# 迭代全部元素
for item in a.flat:
    print(item)
# flat成一行的数组
print(a.flatten())





