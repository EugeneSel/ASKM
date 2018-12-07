import numpy as np
import math

def Seidel(n, epsilon, A, B):
    print(A)
    print(B)
    x = np.zeros([1, n])
    j = 0
    for j in range(n):
        x[0, j] = B[j]
    norm = np.array([])

    p = 0
    for p in range(n):
        j = 0
        q = 0
        r = 0
        for j in range(n):
            if A[p, j] == 0:
                q += 1
            if A[j, p] == 0:
                r += 1
        if q == n or r == n:
            return "This method is not suitable for solving the current example"

    p = 0
    A_old = np.zeros([n])
    B_old = 0
    for p in range(n):
        if A[p, p] == 0:
            j = 0
            for j in range(n):
                if j != p and A[j, p] != 0:
                    q = 0
                    for q in range(n):
                        A_old[q] = A[p, q]
                    B_old = B[p]
                    A[p] = A[j]
                    B[p] = B[j]
                    A[j] = A_old
                    B[j] = B_old
                    break

    i = 0
    while 1:
        summary1 = 0
        k = 0
        x_old = np.zeros([n])
        j = 0
        for j in range(n):
            x_old[j] = x[i, j]
        for k in range(n):
            b = B[k]
            j = 0
            for j in range(n):
                if k != j:
                    b -= A[k, j] * x[i, j]
            x[i, k] = b / A[k, k]
            summary1 += (x[i, k] - x_old[k]) ** 2
        norm = np.append(norm, [math.sqrt(summary1)], axis = 0)
        i += 1
        print("\n")
        print(norm[i - 1])
        x = np.append(x, [x[i - 1]], axis = 0)
        x[i - 1] = x_old
        print("\n")
        print("Number of iteration: ", i)
        print(x)
        if norm[i - 1] > norm[i - 2] and i > 3:
            return "The solution is divergent. This method is not suitable for solving the current example"
        if norm[i - 1] < epsilon:
            break

    return(x[i])