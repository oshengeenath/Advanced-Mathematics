import math
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

x = sym.symbols('x')
eq7 = x*sym.cos(x/2)
f7 = sym.lambdify(x, eq7, 'numpy')
range_7 = np.arange(-5*math.pi, 7*math.pi, 0.01)
y7 = f7(range_7)
plt.plot(range_7, y7)
plt.show()
