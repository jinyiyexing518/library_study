import numpy as np

# 相关联的复制
a = np.arange(4)
b = a
c = a
d = b
a[0] = 1
print(a)
print(b)

# 不关联的复制copy
b = a.copy()
a[0] = 11
print(a)
print(b)

