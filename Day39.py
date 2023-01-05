#Program to Check Prime Number
num=int(input("Enter a positive number: "))
ans=False
if(num<=0):
    print("Enter a valid positive number.")
    
    
elif(num>0 and num<=9):
    if(num==2 or  num==3 or num==5 or num==7):
        print("Prime Number.")
    else:
        print("Not a prime number.")
        
else:
    for i in range(2,num):
        if(num%i==0):
            ans=True
        else:
            ans=False
    if(ans==True):
        print("Prime number.")
    else:
        print("Not prime.")
            
    