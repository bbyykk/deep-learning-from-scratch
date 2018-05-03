#!/usr/bin/python3
def numerical_diff(f, x):
    h = 1e-4
    d =  (f(x+h) - f(x-h))/(2.0*h)
    return d

def function_1(x):
    return 0.01 * x**2.0

def gradient_descent(f, init_x, lr=0.1, step_num=10000):
    x = init_x

    for i in range(step_num):
        grad = numerical_diff(f, x)
        x -= lr * grad
    return x, f(x)


x1, y1 = gradient_descent(function_1, 10)
print(x1, y1)
x1, y1 = gradient_descent(function_1, -10)
print(x1, y1)
