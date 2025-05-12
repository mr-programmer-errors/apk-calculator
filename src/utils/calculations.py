def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Negative input"
    return x ** 0.5

def logarithm(x):
    if x <= 0:
        return "Error: Non-positive input"
    import math
    return math.log(x)

def sine(x):
    import math
    return math.sin(math.radians(x))

def cosine(x):
    import math
    return math.cos(math.radians(x))