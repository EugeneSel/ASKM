import math

def function(x):
    return x * math.asin(x)

def int_mid_rect(a, b, n):
    h = abs(b - a)/n

    result = 0
    i = 0
    for i in range(n):
        result += function(a + h * (i + 0.5))

    return result*h