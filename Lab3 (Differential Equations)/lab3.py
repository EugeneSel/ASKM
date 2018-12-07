# lab 1; 1 v5

from euler_method import euler

while 1:
    try:
        x0 = float(input("Enter x0 (left border of the segment, from -1000000000 to 1000000000): "))
        if x0 < -1000000000 or x0 > 1000000000:
            print("You entered wrong data\n")
        else:
            break
    except ValueError:
        print("You entered wrong data\n")

while 1:
    try:
        xn = float(input("Enter right border of the segment (from -1000000000 to 1000000000): "))
        if xn < -1000000000 or xn > 1000000000 or xn == x0:
            print("You entered wrong data\n")
        else:
            break
    except ValueError:
        print("You entered wrong data\n")

while 1:
    try:
        y0 = float(input("Enter y0 (from -1000000000 to 1000000000): "))
        if y0 < -1000000000 or y0 > 1000000000:
            print("You entered wrong data\n")
        else:
            break
    except ValueError:
        print("You entered wrong data\n")

while 1:
    try:
        h = float(input("Enter step (from 0.0000001 to 10): "))
        if h < 0.0000001 or h > 10 or h > abs(xn - x0):
            print("You entered wrong data\n")
        else:
            break
    except ValueError:
        print("You entered wrong data\n")

if xn < x0:
    h = -h

x, y = euler(y0, x0, xn, h)

print("\nSolution of differential equation y' = 0.2*x + y^2 with initial condition y(", x0, ") = ", y0, " :")
print("\n x = ", x)
print("\n y = ", y)