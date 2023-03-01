import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

x = sym.symbols('x')
n = sym.symbols('n', integer=True, positive=True)
N = sym.symbols('N', integer=True, positive=True)

# defining equations
eq1 = x ** 2 + 1
eq2 = x * sym.exp(-x)
print(eq1)
print(eq2)

x_values = np.linspace(4 * np.pi, -4 * np.pi, 100)
period = 2 * np.pi


# the function
# f(𝑥) = { 𝑥2 + 1    −𝜋 ≤ 𝑥 < 0
#        { 𝑥∙𝑒−𝑥      0 ≤ 𝑥 ≤ 𝜋

def function(x, upper, down):
    f = 0
    if upper < x < 0:
        f = x ** 2 + 1
    elif 0 <= x <= down:
        f = x * sym.exp(-x)
    elif upper > x:
        x_new = x + period
        f = function(x_new, upper, down)
    elif down < x:
        x_new = x - period
        f = function(x_new, upper, down)
    return f


y_values = [function(i, -np.pi, np.pi) for i in x_values]

# plotting graph
plt.plot(x_values, y_values)
plt.grid(True)
plt.show()
