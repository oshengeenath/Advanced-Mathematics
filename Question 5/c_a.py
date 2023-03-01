import sympy as sp

x = sp.Symbol('x')
function = (1 / (1 + sp.exp(-x)))
function1 = sp.sin(sp.sin(2*x))
sp.plot(function1,(x,-5,5))


