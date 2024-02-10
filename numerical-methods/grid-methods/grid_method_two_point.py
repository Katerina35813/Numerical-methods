import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

import triditional
import functions


if __name__ == "__main__":
    f = functions.z
    L = functions.sin_L

    p = functions.p
    q = functions.q

    a = 0
    b = np.pi

    N = 31
    h = (b - a) / N

    x = np.linspace(a, b, N + 1)

    a = np.zeros(N + 1)
    b = np.zeros(N + 1)
    c = np.zeros(N + 1)
    d = L(x, p, q) * h**2

    for i in range(1, N):
        a[i] = 1 - h / 2 * p(x[i])
        b[i] = -2 + h ** 2 * q(x[i])
        c[i] = 1 + h / 2 * p(x[i])

    b[0] = -1
    c[0] = 1
    d[0] = 1 * h

    a[N] = -1
    b[N] = 1
    d[N] = -1 * h

    y = triditional.solve(a, b, c, d)

    # output
    t = PrettyTable(['i', 'x[i]', 'y[i]', 'f(x)', 'Погрешность'])
    for i in range(N + 1):
        t.add_row([i + 1, x[i], y[i], f(x[i]), abs(f(x[i]) - y[i])])
    print(t)

    plt.plot(x, y)
    plt.plot(x, f(x))
    plt.show()
