# Input Format
# The first line contains the space separated values of 'x' and 'k'.
# The second line contains the polynomial 'P'.


# Output Format
# Print True if P(x)=k. Otherwise, print False.


#Sample input:
# 1  4
# x**3 + x**2 + x + 1

#Sample Output:
#True


inp=list(map(int,input().split(" ")))
val_x=inp[0]
ans=inp[1]
eqn=input()
new_eq=eqn.replace("x",str(val_x))
if(ans==eval(new_eq)):
    print(True)
else:
    print(False)
