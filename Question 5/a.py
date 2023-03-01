import sympy as sp

x = sp.Symbol('x')
function = (1 / (1 + sp.exp(-x)))
sp.plot(function,(x,-8,8))


