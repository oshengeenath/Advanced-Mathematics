import math
import matplotlib.pyplot as plt
import numpy as np


def func_cos(x, n):
    cos_approx = 0
    for i in range(n):
        coef = (-1) ** i
        num = x ** (2 * i)
        denom = math.factorial(2 * i)
        cos_approx += coef * ((num) / (denom))

    return cos_approx


angles = np.arange(-5 * np.pi, 5 * np.pi, 0.1)
t_cos = [func_cos(angle, 60) for angle in angles]
fig, ax = plt.subplots()
ax.plot(angles, t_cos)
ax.set_ylim([-5, 5])
plt.show()
