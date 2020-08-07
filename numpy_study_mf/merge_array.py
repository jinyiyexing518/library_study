import numpy as np


a = np.array([1, 1, 1])
b = np.array([2, 2, 2])

# 上下合并，按行合并
print(np.vstack((a, b)))
# 左右合并，按列合并
print(np.hstack((a, b)))

# 增加维度
# 将行向量变为列向量
print(a[:, np.newaxis])

c = a[np.newaxis, :]
print(np.shape(c))

a = a[:, np.newaxis]
b = b[:, np.newaxis]
print(np.hstack((a, b)))

# 多个array进行合并
# axis=0，按行合并；axis=1，按列合并
print('\n', np.concatenate((a, a, b, b), axis=1))

