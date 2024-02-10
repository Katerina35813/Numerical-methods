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


d = L(x) * h**2
for i in range (1, N):
    a[i] =  (1 - h / 2 * p(x[i]))
    b[i] = (-2 + h * h * q(x[i]))
    c[i] =  (1 + h / 2 * p(x[i]))



b[0] = -c[1] * 3 + a[1]
c[0] = c[1] * 4 + b[1]
d[0] = 1 * (2 * h * c[1]) + d[1]

a[N] = -a[N - 1] * 4 - b[N - 1]
b[N] = a[N - 1] * 3 - c[N]
d[N] = -1 * (2 * h * a[N - 1]) - d[N - 1]
y=progonka.progonka(a, b, c, d)

for i in range(0,N+1):
    print(f'{i}=',i)
    print(f'x[{i}]=',x[i])
    print(f'y[{i}]=',y[i])
    print(f'f[{i}]=',y0(x[i]))
    print('error=',abs(y0(x[i])-y[i]))
