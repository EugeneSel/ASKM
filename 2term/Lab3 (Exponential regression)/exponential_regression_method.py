import scipy

import numpy as np

# y = a * (1 - e ^ (b * x)) + c
# ln(y) = ln(a) + (bx + c)


def exponential_regression(y, x, n):
    y_der = np.zeros(n - 1)
    x_der = np.zeros(n - 1)
    f = np.zeros(n - 1)
    x_avg = 0
    f_avg = 0
    fx_avg = 0
    x2_avg = 0

    for i in range(n - 1):
        y_der[i] = abs(y[i + 1] - y[i]) / abs(x[i + 1] - x[i])
        x_der[i] = abs(x[i + 1] + x[i]) / 2
        f[i] = np.log(y_der[i])
        x_avg += x_der[i]
        f_avg += f[i]
        fx_avg += f[i] * x_der[i]
        x2_avg += x_der[i] ** 2

    b = ((n - 1) * fx_avg - f_avg * x_avg) / ((n - 1) * x2_avg - x_avg ** 2)
    a = (f_avg - b * x_avg) / (n - 1)
    B = -b
    A = np.exp(a) / B
    C = sum(y - A * (1 - np.exp(-B * x))) / n

    error = np.linalg.norm(y - (A * (1 - np.exp(-B * x)) + C)) / np.linalg.norm(y)
    return A, B, C, error
