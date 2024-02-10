#n = int(input('Введите размер матрицы:'))

def progonka(a_, b_, c_, d_):
    n_ = len(a_)
    P = [0]*(n_)
    Q = [0]*(n_)
    c = [0]*(n_)
    b = [0]*(n_)
    a = [0]*(n_)
    d = [0]*(n_)
    m = [0]*(n_)
    P[0] = -c_[0]/b_[0]
    Q[0] = d_[0]/b_[0]

    for i in range(1, n_-1):
        P[i] = -c_[i]/(b_[i] + a_[i] * P[i-1])
        Q[i] = (d_[i] - a_[i] * Q[i-1])/(b_[i] + a_[i] * P[i-1])

    m[n_-1] = (d_[n_-1] - a_[n_-1]*Q[n_-2])/(b_[n_-1]+a_[n_-1]*P[n_-2])
    for i in range(n_-2, -1, -1):
        m[i] = P[i]*m[i+1] + Q[i]
    return m

# for i in range(n-1):
#    c[i] = float(input(f'c[{i}] = '))
#
#
# for i in range(n):
#     b[i] = float(input(f'b[{i}] = '))
#
# for i in range(1,n):
#     a[i] = float(input(f'a[{i}] = '))
#
#
# for i in range(n):
#     d[i] = float(input(f'd[{i}] = '))
#
# progonka(n, a, b, c, d)
#
# for i in range(n):
#     print(f'm[{i}]=', m[i])
