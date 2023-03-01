import sympy as sp
x = sp.Symbol('x')
function5 = sp.Piecewise((2*sp.cos(x + sp.pi/6), x < 0), (x*sp.exp(-0.4*x**2), x < sp.pi), (0, True))
sp.plot(function5,(x,-6,6))



