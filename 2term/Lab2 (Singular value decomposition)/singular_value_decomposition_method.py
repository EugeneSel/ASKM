import numpy as np


def least_squares(X, m, n):
    a0 = np.ones(n)
    b0 = np.ones(m)
    a = np.array([a0])
    b = np.array([b0])
    k = 1
    epsilon = 0.001
    F_new = 0

    while 1:
        a = np.append(a, [np.zeros(n)], axis=0)
        b = np.append(b, [np.zeros(m)], axis=0)
        for i in range(m):
            numerator = 0
            denominator = 0
            for j in range(n):
                numerator += X[i, j] * a[k - 1, j]
                denominator += a[k - 1, j] ** 2
            b[k, i] += numerator / denominator

        for j in range(n):
            numerator = 0
            denominator = 0
            for i in range(m):
                numerator += X[i, j] * b[k, i]
                denominator += b[k, i] ** 2
            a[k, j] += numerator / denominator

        F_old = F_new
        F_new = 0
        for i in range(m):
            for j in range(n):
                F_new += (X[i, j] - b[k, i] * a[k, j]) ** 2
        F_new /= 2

        if abs(F_new - F_old) < epsilon:
            break
        k += 1

    return b[k], a[k]


def svd(A, m, n):
    X = np.array([A])
    b = np.array([np.zeros(m)])
    a = np.array([np.zeros(n)])
    k = 0
    epsilon = 0.001

    while 1:
        b_new, a_new = least_squares(X[k], m, n)
        b = np.append(b, [b_new], axis=0)
        a = np.append(a, [a_new], axis=0)
        P_new = np.zeros([m, n])
        for i in range(m):
            for j in range(n):
                P_new[i, j] += b[k + 1, i] * a[k + 1, j]
        X_new = X[k] - P_new
        X = np.append(X, [X_new], axis=0)

        norm = 0
        for j in range(n):
            for i in range(m):
                norm += X_new[i, j] ** 2
        norm = np.sqrt(norm)

        if norm < epsilon:
            break
        k += 1

    q = len(b) - 1
    sigma = np.zeros(q)
    p = len(a) - 1
    for l in range(q):
        b_module = 0
        for i in range(m):
            b_module += b[l + 1, i] ** 2
        b_module = np.sqrt(b_module)
        b[l + 1] = b[l + 1] / b_module

        a_module = 0
        for j in range(n):
            a_module += a[l + 1, j] ** 2
        a_module = np.sqrt(a_module)
        a[l + 1] = a[l + 1] / a_module

        sigma[l] = b_module * a_module

    b = np.delete(b, 0, axis=0)
    a = np.delete(a, 0, axis=0)
    print(b, '\n', '\n', sigma, '\n', '\n',  a)
    return b, sigma, a
