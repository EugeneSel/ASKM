# lab 1; 4 v16

import numpy as np
from seidel_method import Seidel

while 1:
    try:
        n = int(input("Enter system dimension(minimum - 2, maximum - 30): "))
        if n < 2 or n > 30:
            print("You entered wrong data\n")
        else:
            break
    except ValueError:
        print("You entered wrong data\n")

while 1:
    try:
        epsilon = float(input("Enter accuracy(minimum - 0.0000000000000001, maximum - 1): "))
        if epsilon > 1 or epsilon < 0.0000000000000001:
            print("You entered wrong data\n")
        else:
            break
    except ValueError:
        print("You entered wrong data\n")

A = np.zeros([n, n])
i = 0
for i in range(n):
    j = 0
    for j in range(n):
        while 1:
            print("Enter element A[", i + 1, "][", j + 1, "](from -1000000000 to 1000000000):")
            try:
                A[i, j] = float(input())
                if A[i, j] > 1000000000 or A[i, j] < -1000000000:
                    print("You entered wrong data\n")
                else:
                    break
            except ValueError:
                print("You entered wrong data\n")
print(A)
B = np.zeros([n])
i = 0
for i in range(n):
    while 1:
        print("Enter element B[", i + 1, "]:")
        try:
            B[i] = float(input())
            if B[i] > 1000000000 or B[i] < -1000000000:
                print("You entered wrong data\n")
            else:
                break
        except ValueError:
            print("You entred wrong data\n")
print(B)

print("\n")
print("System solution: ", Seidel(n, epsilon, A, B))

