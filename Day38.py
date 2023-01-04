#raise error by ourself

num=int(input("Enter a positive number between 1-100: "))
if(num > 100 or num < 1):
    raise ValueError("Entered number is not in range")
else:
    print("Number is",num)
    
list1=[32,53,64,13,67,4,7,1,56]
ind=int(input("Enter the index of list:"))
if(ind > len(list1)):
    raise IndexError("Invalid index.")
else:
    print("This is the value-",list1[ind])