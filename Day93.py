import re


def check(str, pattern):
    if re.search(pattern, str):
        print("Valid String")
    else:
        print("Invalid String")


pattern = re.compile("^[1234]+$")
st = input("Enter String")
check(st, pattern)
