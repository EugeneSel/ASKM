import cust_input
import numpy as np
from artificial_basis_method import artificial_basis, default_simplex

# variant 4/3:

n = cust_input.int_input(1, 5, "Enter the number of different products (from 1 to 5): \n")
m = cust_input.int_input(1, 5, "Enter the number of different machines (from 1 to 5): \n")

Prod = np.zeros([m, n]) # Productivities
Cost = np.zeros([m, n]) # Cost prices
Power = np.zeros([m]) # Power reserves
Plan = np.zeros([n]) # Release plans
X = np.zeros([m * n]) # Answer vector
X_result = np.zeros([m, n]) # Answer matrix

for i in range(m):
    for j in range(n):
        Prod[i, j] = cust_input.int_input(1, 1000, "Enter the quantity of %d product %d machine per unit of time (from 1 to 1000): \n" %(j+1, i+1))

for i in range(m):
    for j in range(n):
        Cost[i, j] = cust_input.float_input(0.01, 1000000, "Enter the cost price of %d product %d machine (from 0.01 to 1000000): \n" %(j+1, i+1))

for i in range(m):
    Power[i] = cust_input.int_input(1, 1000000, "Enter the reserve of power for %d machine (from 1 to 1000000): \n" %(i+1))

for j in range(n):
    Plan[j] = cust_input.float_input(0.1, 1000000, "Enter the release plan of %d product (from 0.1 to 1000000): \n" %(j+1))

objective_function = np.array([0])
artificial_function = np.zeros([m * n + 1])
basic_x = np.zeros([m, m * n + 1])
basic_y = np.zeros([n, m * n + 1])

for i in range(m):
    for j in range(n):
        objective_function = np.append(objective_function, [-Cost[i, j]], axis = 0)

for i in range(m):
    basic_x[i, 0] = Power[i]
    for j in range(n * m):
        if j + 1 > n * i and j + 1 <= n * (i + 1):
            basic_x[i, j + 1] = 1

for j in range(n):
    basic_y[j, 0] = Plan[j]
    k = 0
    for i in range(n * m):
        if i + 1 == (j + 1) + n * k:
            basic_y[j, i + 1] = Prod[k, j]
            k += 1

for i in range(m * n + 1):
    for j in range(n):
        artificial_function[i] += basic_y[j, i]

simplex_table = basic_x

for j in range(n):
    simplex_table = np.append(simplex_table, [basic_y[j]], axis=0)

simplex_table = np.append(simplex_table, [objective_function], axis=0)
simplex_table = np.append(simplex_table, [artificial_function], axis=0)

print(simplex_table)

simplex_table, X = artificial_basis(simplex_table, m, n)
simplex_table, X = default_simplex(simplex_table, m, n, X)

for i in range(m * n):
    if X[i] != 0:
        X_result[divmod(i, n)[0], divmod(i, n)[1]] = simplex_table[int(X[i] - 1), 0]

print("\nValue of the objective function: ", simplex_table[simplex_table.shape[0] - 1, 0])
print("\nX matrix as a result: ")
print(X_result)




