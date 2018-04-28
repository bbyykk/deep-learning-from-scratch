#!/usr/bin/python3
import numpy as np
import matplotlib.pylab as plt

x = np.arange(-0.0, 1.0, 0.001)
delta = 1e-7
y = np.log(x + 1e-7) 
plt.plot(x, y)
plt.ylim(-5, 0)    # siat-tīng y kuainn ê huān-uî
plt.show()
