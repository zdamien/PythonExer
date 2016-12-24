"""Standard change making problem"""

def pennies(n):
    return 1

def nickels(n):
    if n<5:
        return pennies(n)
    else:
        return nickels(n-5)+pennies(n)

def dimes(n):
    if n<10:
        return nickels(n)
    else:
        return dimes(n-10)+nickels(n)

def quarters(n):
    """
>>> quarters(30)
18
>>> quarters(25)
13
>>> quarters(20)
9
    """
    if n<25:
        return dimes(n)
    else:
        return quarters(n-25)+dimes(n)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
