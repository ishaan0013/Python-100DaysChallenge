#Set Methods

set1={1,2,3,9,4,5}
set2={3,6,9,78,23}
set3=set1.union(set2)
# print(set3)

set4=set1.intersection(set2)
# print(set4)

set1.update(set2)
# print(set1)
#this will add all values of set2 into set1

set5=set1.symmetric_difference(set2)
print(set5)
#This will add values which are not common in both set

print(set1.isdisjoint(set2))
#if nothing in common then return TRUE

print(set1.issubset(set2))

set1.remove(1)
print(set1)
#remove & discard are same but is there is no element then remove will throw error while discard does not.