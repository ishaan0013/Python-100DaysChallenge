#program to display all integers within the range n-m whose sum of digits is an even number
lwr=int(input("Enter lower number: "))
upr=int(input("Enter upper number: "))
if(lwr>upr or lwr<0):
    print("Please provide valid input.")
else:
    for i in range(lwr,upr):
        num = i
        sum = 0
        while(num!=0):
            digit = num%10
            sum = sum + digit
            num = num//10
        if(sum%2==0):
            print(i,end=" ")