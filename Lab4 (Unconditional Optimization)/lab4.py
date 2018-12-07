import cust_input
import numpy as np
from hooke_jeeves_method import hooke_jeeves

# variant 28:
# f(x) = x1^2 + 16x2^2

n = 2
x0 = np.zeros([n])
print(x0)
delta_x = np.zeros([n])
alpha = 2

print("Enter the starting point coordinates:\n")
for i in range(n):
    x0[i] = cust_input.float_input(-1000000000, 1000000000, "Enter %d coordinate (from -1000000000 to 1000000000):\n" %(i+1))

epsilon = cust_input.float_input(0.0000000001, 1, "Enter accuracy (from 0.0000000001 to 1):\n")

print("Enter step sizes:\n")
for i in range(n):
    delta_x[i] = cust_input.float_input(0.00001, 1, "Enter step size for %d coordinate (from 0.00001 to 1):\n" %(i+1))

print("\nMinimum point: ", hooke_jeeves(x0, delta_x, epsilon, alpha))