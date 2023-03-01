import math
import matplotlib.pyplot as plt
import numpy as np


def func_cos(x, n):
    cos_approx = 0
    for i in range(n):
        coef = (-1) ** i
        num = x ** (2 * i)
        denom = math.factorial(2 * i)
        cos_approx += (coef) * ((num) / (denom))

    return cos_approx


angle_rad = (math.radians(30))
coefficient_term = math.radians(60)

out_new = coefficient_term * func_cos(angle_rad, 5)
print(out_new)

angles_d = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
p_cos_d = np.cos(angles_d)
t_cos_d = [coefficient_term * func_cos(angle, 3) for angle in angles_d]

fig, ax = plt.subplots()
ax.plot(angles_d, p_cos_d)
ax.plot(angles_d, t_cos_d)
ax.set_ylim([-10, 10])
ax.legend(['Taylor Series - 3 terms', 'cos() function'])

plt.show()

original_value = coefficient_term * math.cos(angle_rad)
print(original_value)
