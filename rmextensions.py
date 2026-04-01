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

"""
Geometry
"""

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

"""
Stats
"""

def mean(x: list):
    z = 0
    try:
        for i in range(len(set)):
            z += x[i]
        return z / len(set)
    except TypeError: raise TypeError("Error, input must be a valid list")


"""
Linear algebra
"""
def linequ_get_x(z: str, y):
    try:
        # making sure only valid equations exist
        if '+' not in z and '-' not in z: return ValueError("Error, invalid equation")
        if '+' in z and '-' in z: return ValueError("Error, invalid equation")
        # get a and b
        x_const = float(z[z.find('x') - 1])

        #check if there is a, otherwise set x_const to 1
        if z.find('x') - 1 == -1: x_const = 1
        else: x_const = float(z[z.find('x') - 1])

        # check if - is found
        if '-' in z:
            const = float(z[z.find('-') + 1])
            return (y + const) / x_const
        if '+' in z:
            const = float(z[z.find('+') + 1])
            return (y - const) / x_const

    except ValueError:
        return ValueError("Error, invalid equation")


def linequ_get_y(z: str, x):
    try:
        if '+' not in z and '-' not in z: return ValueError("Error, invalid equation")
        if '+' in z and '-' in z: return ValueError("Error, invalid equation")

        if z.find('x') - 1 == -1: x_const = 1
        else: x_const = float(z[z.find('x') - 1])

        if '-' in z:
            const = float(z[z.find('-') + 1])
            return (x_const*x) - const
        if '+' in z:
            const = float(z[z.find('+') + 1])
            return (x_const*x) + const


    except: return ValueError("Error, invalid equation")


def linequ_get_b(z: str, y, x):
    try:
        if '+' not in z and '-' not in z: return ValueError("Error, invalid equation")
        if '+' in z and '-' in z: return ValueError("Error, invalid equation")

        if z.find('x') == -1: a = 1
        else: a = float(z[z.find('x') - 1])

        if '-' in z:
            return y - (a * x)
        if '+' in z:
            return y - (a * x)


    except: return ValueError("Error, invalid equation")