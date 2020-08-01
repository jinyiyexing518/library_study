import numpy as np


# a = np.arange(2, 14).reshape((3, 4))
# # 打印最小值和最大值索引
# print(np.argmin(a), np.argmax(a))
# print(np.mean(a), a.mean(), np.average(a))
# # 中位数
# print(np.median(a))
# # 按位逐位累加
# print(np.cumsum(a))
# # 按位逐位累差
# print(np.diff(a))
# # 输出非零数
# print(np.nonzero(a))

b = np.arange(14, 2, -1).reshape((3, 4))
print(b)
# 逐行进行排序
print(np.sort(b))
# 矩阵转置
print(np.transpose(b))
print((b.T).dot(b))
# 截矩阵
print(np.clip(b, 5, 9))
# 指定axis
print(np.mean(b, axis=0))




