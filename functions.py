# see README.md for information on why each design choice was made

def multiply(a, b):
    result = 0
    if b > 0:
        while b > 0:
            result += a
            b -= 1
        return result
    elif a == 0 or b == 0:
        return 0
    elif b < 0:
        while b < 0:
            result -= a
            b += 1
        return result

def divide(a, b): # WIP
    result = 0

def absolute(a):
    if a >= 0:
        return a
    return (0 - a)

def invert(a):
    return (0 - a)