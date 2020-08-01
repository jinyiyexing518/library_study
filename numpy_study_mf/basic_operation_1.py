import numpy as np


# 按项运算
# a = np.array([10, 20, 30, 40])
# b = np.arange(4)
# # c = a - b
# # c = b**2
# # c = a * b
# # c = 10 * np.sin(a)
# c = b[b < a]
# print(b < 3)
# print(c)

# 矩阵乘法
# a = np.array([[1, 1],
#               [0, 1]])
# b = np.arange(4).reshape((2, 2))
# # 逐项相乘
# c = a * b
# # 矩阵乘法
# c_dot = np.dot(a, b)
# # 另一种形式
# c_dot_2 = a.dot(b)
# print(c)
# print(c_dot)
# print(c_dot_2)

# 随机生成
a = np.random.random((2, 4))
print(a, np.sum(a, axis=1), np.max(a, axis=0), np.min(a))




