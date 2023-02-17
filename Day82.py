# Palindrome Program
def pal(num):
    x1 = num[::-1]
    if x1 == num:
        print("palindrome")
    else:
        print("not a palindrome")


inp = input("Enter the word:\n")
pal(inp)
