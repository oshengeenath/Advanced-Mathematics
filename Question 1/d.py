import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x = sym.symbols('x')
eq1 = x**2 + 1
eq2 = x*sym.exp(-x)

n = sym.symbols('n', integer=True, positive=True)
a0 = (1/(2*sym.pi))*(eq1.integrate((x,-sym.pi,0))+eq2.integrate((x,0,sym.pi)))


an = (1/sym.pi)*(sym.integrate(eq1*sym.cos(n*x), (x,-sym.pi,0))+sym.integrate(eq2*sym.cos(n*x), (x,0,sym.pi)))
bn = (1/sym.pi)*(sym.integrate(eq1*sym.sin(n*x), (x,-sym.pi,0))+sym.integrate(eq2*sym.sin(n*x), (x,0,sym.pi)))

def f(x):
    return np.where((x>= -np.pi)&(x<0),(x**2)+1,np.where((x>=0)&(x<np.pi),x*np.exp(-x),0))

def har(x,n):
    return np.sin(n*x)/n

def rmse(f,har,x):
    return np.sqrt(np.mean(np.square(f-har)))

xrange = np.linspace(-4*np.pi, 4*np.pi, 1000)

rmseVal = []
for n in range(1,151):
    rmseVal.append(rmse(f(xrange),har(xrange,n),xrange))

print("RMSE for 1st harmonic: ", rmseVal[0])
print("RMSE for 5th harmonic: ", rmseVal[4])
print("RMSE for 150th harmonic: ",rmseVal[149])

plt.plot(rmseVal)
plt.xlabel('harmonics')
plt.ylabel('RMSE')
plt.show()