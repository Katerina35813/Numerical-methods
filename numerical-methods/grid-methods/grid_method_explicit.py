import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

import triditional
import functions


if __name__ == "__main__":
    f = functions.cos
    L = functions.cos_L

    p = functions.p
    q = functions.q

    a = 0
    b = np.pi

    alpha = [1, 1]
    betta = [0, 0]
    gamma = [f(a), f(b)]

    N = 32
    h = (b - a) / N

    x = np.linspace(a, b, N + 1)

    a = np.zeros(N + 1)
    b = np.zeros(N + 1)
    c = np.zeros(N + 1)
    d = L(x, p, q)

    for i in range(1, N):
        a[i] = (1 - h / 2 * p(x[i])) / h**2
        b[i] = (-2 + h**2 * q(x[i])) / h**2
        c[i] = (1 + h / 2 * p(x[i])) / h**2

    b[0] = alpha[0] - betta[0] / h
    c[0] = betta[0] / h
    d[0] = gamma[0]

    b[N] = alpha[1] - betta[1] / h
    a[N] = betta[1] / h
    d[N] = gamma[1]

    y = triditional.solve(a, b, c, d)

    # output
    t = PrettyTable(['i', 'x[i]', 'y[i]', 'f(x)', 'Погрешность'])
    for i in range(N + 1):
        t.add_row([i + 1, x[i], y[i], f(x[i]), abs(f(x[i]) - y[i])])
    print(t)

    plt.plot(x, y)
    plt.plot(x, f(x))
    plt.show()
