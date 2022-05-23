import numpy as np
import matplotlib.pyplot as plt
import os

data_path = os.getcwd()


def calc_left_corner(u0r, u0l, h, tau):
    return (u0r + tau / h * u0l) / (1 + tau / h)


def implicit_left_def(num, T, courant, an):
    u0 = [1. if num * 0.1 < n <= num * 0.2 else 0. for n in range(num + 2)]
    u = np.zeros(num + 2)
    x = np.linspace(0, 1, num + 2)
    x_an = np.linspace(0, 1, 101)
    time = 0
    h = 1 / num
    tau = courant * h
    while time <= T:
        for i in range(1, num + 1):
            u[i] = calc_left_corner(u0[i], u[i-1], h, tau)
        for i in range(0, num):
            u0[i] = u[i]
        time += tau
    plt.title('Linear advection')
    plt.xlabel('x coordinate')
    plt.ylabel('function value')
    plt.grid()
    plt.plot(x, u0, label='Left implicit corner')
    if an == 1:
        u_an = [1. if (0.1 + T) * 100 < n <= (0.2 + T) * 100 else 0. for n in range(101)]
        plt.plot(x_an, u_an, label='Analytic')
    plt.legend()
    plt.savefig(data_path + r"\static\plot(1).png", format="png", dpi=500)
    plt.close()


implicit_left_def(500, 0.5, 1.5, 1)
