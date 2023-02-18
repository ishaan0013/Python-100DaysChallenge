# Program to determine whether the given number is a Harshad Number.
# If a number is divisible by the sum of its digits, then it will be known as a Harshad Number.
num = int(input("Enter the number:\n"))
rem = sum = 0

# Make a copy of num and store it in variable n
n = num

# Calculates sum of digits
while num > 0:
    rem = num % 10
    sum = sum + rem
    num //= 10

# Checks whether the number is divisible by the sum of digits
if n % sum == 0:
    print(f"{n} is a harshad number")
else:
    print(f"{n} is not a harshad number")
