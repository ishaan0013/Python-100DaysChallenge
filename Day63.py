#GCD



def hcf(a, b):
	if(b == 0):
		return abs(a)
	else:
		return hcf(b, a % b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


print(f"The gcd of {a} and {b} is : ", end="")
print(hcf(a,b))
