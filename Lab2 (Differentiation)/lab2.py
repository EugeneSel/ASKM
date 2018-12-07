# lab 2; 3 v17

from integration_middle_rectagles_method import int_mid_rect

while 1:
    try:
        a = float(input("Enter lower border of the integral (from -1 to 0.999999999): "))
        if a < -1 or a > 0.999999999:
            print("You entered wrong data\n")
        else:
            break
    except ValueError:
        print("You entered wrong data\n")

while 1:
    try:
        b = float(input("Enter higher border of the integral (from -0.999999999 to 1): "))
        if b < -0.999999999 or b > 1:
            print("You entered wrong data\n")
        elif b < a:
            print("Higher border can`t be less than lower border. Please, repeat entering of the higher border of the integral:\n")
        else:
            break
    except ValueError:
        print("You entered wrong data\n")

while 1:
    try:
        n = int(input("Enter number of grid intervals (from 10 to 1000000): "))
        if n < 10 or n > 1000000:
            print("You entered wrong data\n")
        else:
            break
    except ValueError:
        print("You entered wrong data\n")

print("\nResult of the integral x*arcsin(x) from", a, " to ", b," equals ", int_mid_rect(a, b, n))