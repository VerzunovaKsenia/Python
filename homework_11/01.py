#
import numpy as np


def left_corner (t, u0p, u01):
    h = 0.01
    t = t / 100
    return u0p + t * (u01 - u0p)/h


u0 = [1 if 10 < n <= 20 else 0 for n in range(101)]
u = np.zeros(101)

for time in range(1000, 5000):
    for i in range(1, 101):
        u[i] = left_corner(time, u0[i], u0[i - 1])
    for i in range(0, 100):
        u0[i] = u[i]
    print(u)
###

