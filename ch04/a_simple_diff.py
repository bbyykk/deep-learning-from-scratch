#!/usr/bin/python3
def func_y(x):
    return x**2.0

def numerical_diff(f, x):
    h = 1e-4
    d =  (f(x+h) - f(x-h))/(2.0*h)
    return d

print(numerical_diff(func_y, 0.5))
print(numerical_diff(func_y, 0))
