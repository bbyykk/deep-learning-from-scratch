#!/usr/bin/python3
import numpy as np
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

y1 = [0.0, 0.0, 0.2, 0.69999999, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
t1 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
y2 = [0.0, 0.0, 0.0, 0.0, 0.89999998, 0.1, 0.0, 0.0, 0.0, 0.0]
t2 = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0] 

print(mean_squared_error(np.array(y1), np.array(t1)))
print(mean_squared_error(np.array(y2), np.array(t2)))
