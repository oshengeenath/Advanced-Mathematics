import sympy as sp
x = sp.Symbol('x')
function4 = x**2 * sp.cos(sp.cos(2*x)) - 2 * sp.sin(sp.sin(x - sp.pi/3))
sp.plot(function4,(x,-5,5))





