import numpy as np


# 默认int32， float64
a = np.array([2.0, 23, 4], dtype=np.int64)
print(a, a.dtype)

b = np.zeros((3, 4))
print(b, b.dtype)

c = np.ones((3, 4), dtype=np.float)
print(c, c.dtype)

d = np.empty((3, 4))
print(d, d.dtype)

e = np.arange(10, 20, 2)
print(e, e.dtype)

f = np.arange(12)
f = np.reshape(f, (3, 4))
print(f, f.shape)

# 生成线段
g = np.linspace(1, 10, 20).reshape((4, 5))
print(g, g.shape)

