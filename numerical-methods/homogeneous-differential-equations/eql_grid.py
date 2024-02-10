import numpy as np
import progonka

def p(x):
    return (-np.sin(x))

def q(x):
    return (np.cos(x))

def y2(x):
    return (-np.sin(x))

def y1(x):
    return (np.cos(x))

def y0(x):
    return (np.sin(x))

def L(x):
    return (y2(x)+p(x)*y1(x)+q(x)*y0(x))



N=35
A=0
B=np.pi
h = (B-A) / N
x = np.linspace(A, B, N + 1)

a = [0]*(N+1)
b = [0]*(N+1)
c = [0]*(N+1)
d = [0]*(N+1)
alpha=[1,1]
betta=[0,0]
gamma=[y0(A),y0(B)]

for i in range (1, N):
    a[i] =  (1 - h / 2 * p(x[i]))/h**2
    b[i] = (-2 + h * h * q(x[i]))/h**2
    c[i] =  (1 + h / 2 * p(x[i]))/h**2

d = L(x)

b[0] = alpha[0] - betta[0] / h
c[0] = betta[0] / h
d[0] = gamma[0]

b[N] = alpha[1] - betta[1] / h
a[N] = betta[1] / h
d[N] = gamma[1]
y=progonka.progonka(a, b, c, d)

for i in range(0,N+1):
    print(f'{i}=',i)
    print(f'x[{i}]=',x[i])
    print(f'y[{i}]=',y[i])
    print(f'f[{i}]=',y0(x[i]))
    print('error=',abs(y0(x[i])-y[i]))
