#docstring
def square(b):
    """This function is for squaring a number"""
    a=b**2
    return a
n=int(input())
print(square(n))
print(square.__doc__)