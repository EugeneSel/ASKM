import numpy as np


def tridiagonal_matrix(n, a, b, c, d):
    x = np.zeros(n)
    alpha = np.zeros(n)
    beta = np.zeros(n)

    alpha[0] = -c[0]/b[0]
    beta[0] = d[0]/b[0]

    for i in range(1, n - 1, 1):
        alpha[i] = -c[i]/(a[i] * alpha[i - 1] + b[i])
        beta[i] = (d[i] - a[i] * beta[i - 1])/(a[i] * alpha[i - 1] + b[i])

    x[n - 1] = (d[n - 1] - a[n - 1] * beta[n - 2])/(a[n - 1] * alpha[n - 2] + b[n - 1])

    for i in range(n - 2, -1, -1):
        x[i] = alpha[i] * x[i + 1] + beta[i]

    return x
