import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

import triditional
import functions


if __name__ == "__main__":
    f = functions.sin
    L = functions.sin_L

    p = functions.p
    q = functions.q

    a = 0
    # b = 1
    b = np.pi

    N = 30
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

    b[0] = -c[1] * 3 + a[1]
    c[0] = c[1] * 4 + b[1]
    d[0] = 1 * (2 * h * c[1]) + d[1]

    a[N] = -a[N - 1] * 4 - b[N - 1]
    b[N] = a[N - 1] * 3 - c[N]
    d[N] = -1 * (2 * h * a[N - 1]) - d[N - 1]

    y = triditional.solve(a, b, c, d)

    # output
    t = PrettyTable(['i', 'x[i]', 'y[i]', 'f(x)', 'Погрешность'])
    for i in range(N + 1):
        t.add_row([i + 1, x[i], y[i], f(x[i]), abs(f(x[i]) - y[i])])
    print(t)

    plt.plot(x, y)
    plt.plot(x, f(x))
    plt.show()
