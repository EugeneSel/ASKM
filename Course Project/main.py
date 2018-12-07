import numpy as np
import cust_input
from matplotlib import pyplot as plt

n = 8
T_theor = 2.36

def least_squares (y, sse):
    A = np.array([[0.0, 0.0], [0.0, 0.0]])
    B = np.array([0.0, 0.0])

    for i in range(n):
        B[0] += 2 * sse[i]
        B[1] += 2 * sse[i]/y[i]
        A[0, 0] += 2
        A[0, 1] += 2/y[i]
        A[1, 0] += 2/y[i]
        A[1, 1] += 2/y[i] ** 2

    det = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    det1 = B[0] * A[1, 1] - A[0, 1] * B[1]
    det2 = A[0, 0] * B[1] - B[0] * A[1, 0]
    a0 = det1/det
    a1 = det2/det

    return a0, a1


y = np.zeros([n])
sse = np.zeros([n])

print("\nEnter the start data:")
for i in range(n):
    y[i] = cust_input.int_input(0, 1000000, "Enter the volume of production for the %d quarter:" %(i+1))
    sse[i] = cust_input.int_input(0, 1000000000, "Enter the cost per unit of production for the %d quarter:" %(i+1))

print(y)
print(sse)

plt.scatter(y, sse, marker='o', color='blue')
plt.grid()
plt.xlabel("Обсяг виробництва")
plt.ylabel("Собівартість")
plt.show()

#sse = a0 + a1/y

a0, a1 = least_squares(y, sse)

print(a0, a1)

a0_avg = 0
for i in range(n):
    a0_avg += sse[i] - a1/y[i]
a0_avg /= n

a1_avg = 0
for i in range(n):
    a1_avg += y[i] * (sse[i] - a0)
a1_avg /= n

a0_dev = 0
for i in range(n):
    a0_dev += ((sse[i] - a1/y[i]) - a0_avg) ** 2
a0_dev = np.sqrt(a0_dev/(n - 1))

a1_dev = 0
for i in range(n):
    a1_dev += (y[i] * (sse[i] - a0) - a1_avg) ** 2
a1_dev = np.sqrt(a1_dev/(n - 1))

print(a0_dev, a1_dev)

y_avg = 0
for i in range(n):
    y_avg += y[i]/n

S_y = 0
for i in range(n):
    S_y += (y[i] - y_avg) ** 2
S_y = np.sqrt(S_y/(n - 1))

sse_avg = 0
for i in range(n):
    sse_avg += sse[i]/n

S_sse = 0
for i in range(n):
    S_sse += (sse[i] - sse_avg) ** 2
S_sse = np.sqrt(S_sse/(n - 1))

T0 = np.abs(a0_avg - a0) * np.sqrt(n)/a0_dev
T1 = np.abs(a1_avg - a1) * np.sqrt(n)/a1_dev

print(y_avg, sse_avg)
print(S_y, S_sse)
print(T0, T1)

if T0 < T_theor:
    print("\nCoefficient a0 is significant")
else:
    print("\nCoefficient a0 is insignificant")

if T1 < T_theor:
    print("\nCoefficient a1 is significant")
else:
    print("\nCoefficient a1 is insignificant")