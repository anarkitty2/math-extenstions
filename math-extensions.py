# Constants
PI = 3.14159265

def fact(n: int):
    temp = n
    try:
        while n > 0:
            temp *= n
            n -= 1
        return temp
    except ZeroDivisionError: raise ZeroDivisionError("Error, area must be a valid integer or float")
    except TypeError: raise TypeError("Error, area must be a valid integer or float")


def circumference(r):
    try:
        if r <= 0: return ValueError("Error, radius must be positive")
        return 2 * PI * r
    except ValueError: raise ValueError("Error, radius must be a valid integer or float")


def c_area(r):
    try:
        if r <= 0: return "Error, radius must be positive"
        return PI * (r**2)
    except ValueError: raise ValueError("Error, radius must be a valid integer or float")


def s_area(r):
    try:
        if r <= 0: raise ValueError("Error, radius must be a valid integer or float")
        return 4*PI*(r**2)
    except ValueError: raise ValueError("Error, radius must be a valid integer or float")


def mean(x: list):
    z = 0
    try:
        for i in range(len(set)):
            z += x[i]
        return z / len(set)
    except TypeError: raise TypeError("Error, input must be a valid list")


def linequ_get_x(z: str, y):
    try:
        if 'x' not in z: return ValueError("Error, invalid equation")
        # get a and b
        x_const = float(z[z.find('x') - 1])
        const = float(z[z.find('+') + 1])

        return (y-const)/x_const
    except TypeError: raise TypeError("Error, inputs must be a valid string")
