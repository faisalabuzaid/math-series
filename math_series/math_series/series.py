def fibonacci(n):
    """ this function take index and return Fibonacci sequence """
    x, y = 0, 1
    for i in range(n):
        x, y = y, y+x
    return x


def lucas(n):
    """ this function take index and return Lucas sequence """
    x, y = 2, 1
    for i in range(n):
        x, y = y, y+x
    return x

def sum_series(n, x=0, y=1):
    """ Calling this function with no optional parameters will produce numbers from the fibonacci series.
    Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers.
    Other values for the optional parameters will produce other series."""
    for i in range(n):
        x, y = y, y+x
    return x

print(lucas(10))