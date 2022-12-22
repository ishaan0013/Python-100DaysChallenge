#list in python

list1 = [1,2,3,65,6765,"Ishaan","age22",True,99,90,{'hello', 'bye'},(1,2,3,4,),False]
print(len(list1))
print(type(list1))
print(list1[5])

if "Ishaan" in list1:
    print("yes")
else:
    print("No")
    
if "aan" in "Ishaan":
    print("HAANN")
else:
    print("NAHIII")     
print(list1)    
print(list1[1:len(list1)-1])
print(list1[0:11:2])
