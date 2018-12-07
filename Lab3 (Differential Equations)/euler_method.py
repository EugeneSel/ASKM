def function(x, y):
    return 0.2*x + y ** 2

def euler(y0, x0, xn, h):
    x = x0
    y = y0

    n = round(abs(xn - x0)/h)

    print("\n x, y")
    i = 0
    for i in range(n):
        y += h * function(x, y)
        x += h
        print(x, y)

    return x, y