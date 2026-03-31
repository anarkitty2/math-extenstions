PI = 3.14159265

def fact(n: int):
    temp = n
    try:
        while n > 0:
            temp *= n
            n -= 1
        return temp
    except ZeroDivisionError:
        raise ValueError("Error, area must be a valid integer or float")
    except TypeError:
        raise TypeError("Error, area must be a valid integer or float")


def circumference(r):
    try:
        if r <= 0: return "Error, circumference must be positive"
        return 2 * PI * r
    except ValueError:
        raise ValueError("Error, area must be a valid integer or float")


def c_area(r):
    try:
        if r <= 0: return "Error, area must be positive"
        return PI * (r**2)
    except ValueError:
        raise ValueError("Error, area must be a valid integer or float")


def s_area(r):
    try:
        if r <= 0: raise ValueError("Error, area must be a valid integer or float")
        return 4*PI*(r**2)
    except ValueError:
       raise ValueError("Error, area must be a valid integer or float")
