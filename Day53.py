#Map, Filter & Reduce function
from functools import reduce
list1=[1,2,4,6,8,2,9,12,76]

ans=list(map(lambda x: x*x,list1))
print(ans)
    
    
ans2=list(filter(lambda x: x>10,list1))
print(ans2)

ans3=reduce(lambda x,y: x+y,list1)
print(ans3)