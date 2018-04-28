#!/usr/bin/python3
import numpy as np
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y+delta))

y1 = [0.0, 0.0, 0.2, 0.69999999, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
t1 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
y2 = [0.0, 0.0, 0.0, 0.0, 0.89999998, 0.1, 0.0, 0.0, 0.0, 0.0]
t2 = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0] 

print(cross_entropy_error(np.array(y1), np.array(t1)))
print(cross_entropy_error(np.array(y2), np.array(t2)))
