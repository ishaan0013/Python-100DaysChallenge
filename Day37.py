#finally clause
def exc():
    try:
        lst=[5,6,7,8,3,2,1,3,6,7,3]
        print(lst)
        ind=int(input("Enter the index of list which you want to see : "))
        print(lst[ind])
        return 1
    except IndexError:
        print("Invalid index")
        return 0
    finally:
        print("I am always executed")

ans=exc()
print(ans)
