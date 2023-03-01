# parameters which can be used to adjust to change the shape of logistic functions
import sympy as sp

x = sp.Symbol('x')
function1 = (1 / (1 + sp.exp(-x)))
function2 = -x ** 3 - 2 * x ** 2 + 3 * x + 10
function3 = sp.exp(-0.8 * x)
function4 = x ** 2 * sp.cos(sp.cos(2 * x)) - 2 * sp.sin(sp.sin(x - sp.pi / 3))
function5 = sp.Piecewise((2 * sp.cos(x + sp.pi / 6), x < 0), (x * sp.exp(-0.4 * x ** 2), x < sp.pi), (0, True))

x0 = 0
l = 1
k = 1


# logistic function
def logistic_function(x, l, x0, k):
    return l / (1 + sp.exp(-k * (x - x0)))


g1 = logistic_function(function1, l, x0, k)
sp.plot(g1, (x, -5, 5))
g2 = logistic_function(function2, l, x0, k)
sp.plot(g2, (x, -5, 5))
g3 = logistic_function(function3, l, x0, k)
sp.plot(g3, (x, -5, 5))
g4 = logistic_function(function4, l, x0, k)
sp.plot(g4, (x, -5, 5))
g5 = logistic_function(function5, l, x0, k)
sp.plot(g5, (x, -5, 5))
