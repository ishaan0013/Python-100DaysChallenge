#Program to Convert Decimal to Binary Using Recursion

def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

dec =int(input("Enter decimal number: "))

convertToBinary(dec)
print()
