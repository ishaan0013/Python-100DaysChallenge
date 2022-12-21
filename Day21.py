#types of function arguments
# 1 -Default argument
# 2 -Keyword arguments (named arguments)
# 3 -Positional arguments
# 4 -Arbitrary arguments 

def add(a,b=10):
    c = a+b
    return c
sum = add(5)
print('sum is',sum)
#here b is default argument

def average(a,b):
    c = (a+b)/2
    return c
av = average(b=10,a=20)
print('average is',av)
#keyword argument