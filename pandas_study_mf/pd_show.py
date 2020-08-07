import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()
data.plot()

data2 = pd.DataFrame(np.random.randn(1000, 4),
                     index=np.arange(1000),
                     columns=list("ABCD"))
data2 = data2.cumsum()
data2.plot()

# plot methods:
# 'bar', 'hist', 'box', 'ked', 'aera', 'scatter', 'hexbin', 'pie'

ax = data2.plot.scatter(x='A', y='B', color='DarkBlue', label='Class1')
data2.plot.scatter(x='A', y='C', color='DarkGreen', label='Class2', ax=ax)

plt.show()

















