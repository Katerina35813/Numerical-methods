import numpy as np


functions = [
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


func = functions[0]
u = func["u"]
psi = func["psi"]
phi = func["phi"]

h = 0.1
tau = 0.005

r = tau / h ** 2


a = 0
b = 10

T = 0.5

x = np.arange(a, b, h)
t = np.arange(0, T, tau)

n0 = 5
m0 = 5

U = np.zeros((len(t), len(x)))
U[0] = psi(x)

for n in range(1, n0 + 1):
    for m in range(m0 - n0 + n, m0 + n0 + 1 - n):
        U[n][m] = r * (U[n - 1][m - 1] + U[n - 1][m + 1]) + (1 - 2 * r) * U[n - 1][m] + tau * phi(x[m], t[n - 1])

print("Наша функция:", func["f"])
print(U[0:n0+1,0:m0+n0+1].transpose())
print('Приближенное решение:',U[n0][m0])
print("Точное решение:", np.around(u(x[m0], t[n0]), 7))
print("Погрешность вычислений: ", abs(u(x[m0], t[n0]) - U[n0][m0]))
