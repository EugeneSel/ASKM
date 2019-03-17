from singular_value_decomposition_method import svd
import cust_input
import numpy as np
from numpy import linalg


m = cust_input.int_input(2, 10, "Enter the number of equations (from 2 to 10):\n")
n = cust_input.int_input(2, 10, "Enter the number of unknown variables (from 2 to 10):\n")

A = np.zeros([m, n])
B = np.zeros([m, 1])

print("Enter coefficients next to unknown:\n")
for i in range(m):
    for j in range(n):
        A[i, j] = cust_input.float_input(-1000000, 1000000, "Enter coefficient [%d, %d]:\n" %(i + 1, j + 1))

print("Enter free coefficients:\n")
for i in range(m):
    B[i, 0] = cust_input.float_input(-1000000, 1000000, "Enter coefficient [%d]:\n" %(i + 1))

U, S, V = svd(A, m, n)

mU = np.matrix(U)
mB = np.matrix(B)
mV = np.matrix(V.transpose())

K = mU * mB
for i in range(min(m, n)):
    K[i, 0] /= S[i]
X = mV * K
print("\nThe answer is: \n", X)

B_exp = A * X

relative_fault = linalg.norm(B - B_exp) / linalg.norm(B)

print("\nRelative fault for current result equals: \n", relative_fault)
