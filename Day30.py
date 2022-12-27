#recursion
def factoial(f):
    """This function finds the factorial of a given number"""
    if(f==1 or f==0):
        return 1
    elif(f<0):
        return 0
    else:
        return(f*factoial(f-1))

f=int(input())
print(factoial(f))
print(factoial.__doc__)