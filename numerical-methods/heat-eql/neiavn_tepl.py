import numpy as np
import progonka

list = [
    {
        "f": "tx³+x²",
        "u": lambda _x, _t: _t * _x ** 3 + _x ** 2,
        "psi": lambda _x: _x ** 2,
        "phi": lambda _x, _t: _x ** 3 - 6 * _t * _x - 2
    },
    
    {
        "f": "tcos(x)+x",
        "u": lambda _x, _t: _t * np.cos(_x) + _x,
        "psi": lambda _x: _x,
        "phi": lambda _x, _t: np.cos(_x) + _t * np.sin(_x) - 1
    }
]

func = list[0]

u = func["u"]
psi = func["psi"]
phi = func["phi"]

h = 0.1
tau = 0.006
r = tau / h ** 2

A = 0
B = 1
T = 1

x = np.arange(A, B, h)
t = np.arange(0, T, tau)

n0 = 4
m0 = 5
leng=len(x)
U = np.zeros((len(t), leng))

U[0] = psi(x)

a = [0]*leng
b = [0]*leng
c = [0]*leng
d = [0]*leng

for i in range(1, n0 + 1):
    a[1] = 0
    b[1] = 2 * r + 1
    c[1] = -r
    d[1] = tau * phi(x[0], t[i]) + U[i - 1, 0]

    a[-1] = -r
    b[-1] = 2 * r + 1
    c[-1] = 0
    d[-1] = tau * phi(x[-1], t[i]) + U[i - 1, -1] + r * (t[i] + 1)

    for j in range(1, leng - 1):
        a[j] = -r
        b[j] = 2 * r + 1
        c[j] = -r
        d[j] = tau * phi(x[j], t[i]) + U[i - 1, j]

    U[i, 1:] = progonka.solve(a[1:], b[1:], c[1:], d[1:])

    print(f'Слой {i}')
    
    for n_ in range(len(U[i])):
        print("x=",x[n_])
        print('u(n0, m0)',U[i, n_] ) 
        print("u(x, t)",u(x[n_], t[i])) 
        print("погрешность=",abs(u(x[n_], t[i]) - U[i, n_])) 
        
    print(' ')

print("Функция:", func["f"])
print("Полученное значение :", U[n0][m0])
print("Точное решение:", u(x[m0], t[n0]))
print("Погрешность: ", abs(u(x[m0], t[n0]) - U[n0][m0]))
