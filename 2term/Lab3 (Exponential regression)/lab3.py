import numpy as np
import cust_input
import random
from exponential_regression_method import exponential_regression
import readchar

n = cust_input.int_input(2, 100, "Enter the number of function and variable values (from 2 to 100): \n")
x = np.zeros(n)
y = np.zeros(n)

print("1 - custom input\n2 - random values\n")
while 1:
    key = input()
    if key == '1' or key == '2':
        break

if key == '1':
    for i in range(n):
        x[i] = cust_input.float_input(-1000000, 1000000, "Enter the %d value of variable: \n" %(i + 1))
        y[i] = cust_input.float_input(-1000000, 1000000, "Enter the %d value of function: \n" % (i + 1))

elif key == '2':
    while 1:
        x_low = cust_input.float_input(-1000000, 1000000,
                                       "Enter the low border of values for variable (from -1000000 to 1000000):\n")
        x_high = cust_input.float_input(-1000000, 1000000,
                                        "Enter the high border of values for variable (from -1000000 to 1000000):\n")
        if x_high > x_low:
            break
        print("High border less than low border. Please, repeat entering:\n")

    while 1:
        y_low = cust_input.float_input(-1000000, 1000000,
                                       "Enter the low border of values for function (from -1000000 to 1000000):\n")
        y_high = cust_input.float_input(-1000000, 1000000,
                                        "Enter the high border of values for function (from -1000000 to 1000000):\n")
        if y_high > y_low:
            break
        print("High border less than low border. Please, repeat entering:\n")

    for i in range(n):
        x[i] = random.uniform(x_low, x_high)
        y[i] = random.uniform(y_low, y_high)

print("x: ", x)
print("f(x): ", y)

A, B, C = exponential_regression(y, x, n)
print("f(x) = %f * (1 - e ^ (%f * x)) + %f" %(A, B, C))
