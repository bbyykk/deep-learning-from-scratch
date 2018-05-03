# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)


def function_1(x):
    return 0.01*x**2 


def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    print(y)
    return lambda t: d*t + y
     
x = np.arange(-10.0, 10.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

for i in [ -5, 0, 5]:
    tf = tangent_line(function_1, i)
    y2 = tf(x)
    plt.plot(x, y)
    plt.plot(x, y2)

plt.show()
