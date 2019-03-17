import cust_input
import numpy as np
from tridiagonal_matrix_method import tridiagonal_matrix

n = cust_input.int_input(2, 100, "Enter matrix dimension (from 2 to 100):\n")

a = np.zeros(n)
b = np.zeros(n)
c = np.zeros(n)
d = np.zeros(n)

print("Enter the elements of tridiagonal matrix:\n")
for i in range(n):
    for j in range(n):
        if i == j + 1:
            a[i] = cust_input.float_input(-1000000, 1000000,
                                          "Enter element [%d, %d] (from -1000000 to 1000000):\n" % (i + 1, j + 1))
        elif i == j:
            b[i] = cust_input.float_input(-1000000, 1000000,
                                          "Enter element [%d, %d] (from -1000000 to 1000000):\n" % (i + 1, j + 1))
        elif j == i+1:
            c[i] = cust_input.float_input(-1000000, 1000000,
                                          "Enter element [%d, %d] (from -1000000 to 1000000):\n" % (i + 1, j + 1))
print(a, b, c)

print("Enter the vector of free coefficients:\n")
for i in range(n):
    d[i] = cust_input.float_input(-1000000, 1000000,
                                          "Enter element %d (from -1000000 to 1000000):\n" % (i + 1))

x = tridiagonal_matrix(n, a, b, c, d)

print("Vector x as a result:\n")
print("x = ", x)
