import sympy as sp

x = sp.Symbol('x')
function = (1 / (1 + sp.exp(-x)))
d = function.diff(x)
sp.plot(d, (x,-8,8))

