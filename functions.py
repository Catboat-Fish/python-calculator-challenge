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

def divide(a, b):
    quotient = 0
    negative = 0
    # i/0 and 0/i catching
    if b == 0:
        return "Error: cannot divide by zero"
    if a == 0:
        return 0
    # inverts and stores negatives (check README for explanation, this one is important)
    if a < 0:
        a = 0 - a
        negative += 1
    if b < 0:
        b = 0 - b
        negative -= 1
    # larger denominator catching
    if a < b:
        if negative != 0:
            a = invert(a)
        return (f"{a}/{b}")
    # main division loop
    while a >= b:
        a -= b
        quotient += 1
    # inverter
    if negative != 0:
        quotient = invert(quotient)
    # results
    if a != 0:
        return (f"{quotient} {a}/{b}")
    return quotient

def invert(a):
    return (0 - a)

def absolute(a):
    if a >= 0:
        return a
    return invert(a)

def power(a, b):
    # a^b
    original = a
    # if b is negative
    if b < 0:
        return "Error: this function can only do positive powers currently. Sorry about that."
    # if b == 0
    if b == 0:
        return 1
    # else
    while b > 1:
        a = multiply(a, original)
        b -= 1
    return a

def tetrate(a, b):
    pass