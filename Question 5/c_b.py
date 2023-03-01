import sympy as sp

x = sp.Symbol('x')
function2 = -x**3 - 2*x**2 + 3*x + 10
sp.plot(function2,(x,-5,5))


