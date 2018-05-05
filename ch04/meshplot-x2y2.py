# coding: utf-8
# cf.http://d.hatena.ne.jp/white_wheels/20100327/p3
import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


def function_2(x):
    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)


if __name__ == '__main__':
    x0 = np.arange(-3, 3, 0.1)
    x1 = np.arange(-3, 3, 0.1)
    X, Y = np.meshgrid(x0, x1)

    ## This is OK
    Z = X**2 +Y**2 

    ## This have errors
    # ValueError: shape mismatch: objects cannot be broadcast to a single shape
    # Z = function_2(np.array([X, Y])) 
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    surf = ax.plot_surface(X, Y, Z)
    plt.show()
