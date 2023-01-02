# Exception Handling
try:
    num = int(input("Enter an integer: "))
    a=[24,65,32,65]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Invalid index.")
# except Exception as e:
#     print(e)