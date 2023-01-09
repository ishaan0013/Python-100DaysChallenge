# Python program to find H.C.F of two numbers

def hcf(x, y):
    hcf=0
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
if(num1 < 0 or num2 < 0):
    print("Please enter integers greater than 1")
else:
    print("The H.C.F. is", hcf(num1, num2))