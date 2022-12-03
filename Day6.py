print('Welcome in day 5')
#today we learn about variables
# it is just like a container in our home
a = 10
print(a)
#there are several types of data types in python
#like int, float, string, boolean
#example
b= True
c = 'Ishaan'
d = None
e = complex(3,5)

#we can also check these types by:
print("a is of type", type(a))
print("b is of type", type(b))
print("c is of type", type(c))
print("d is of type", type(d))
print("e is of type", type(e))
#everything in python is a object

#there are also list & tuples
#only difference between them is that list is mutable and tuples are immutable
list1 = ['Ishaan','Bhardwaj',2,True,False]
print(list1)

tuple1 = ("hello", "how" , "you", True , 1.32, complex(3,6))
print(tuple1)

#Dictionaries in python used to store data values in key:value pairs.
dict = {'name':'Ishaan','Age':'20','Marks':'500/1000','born year':2000}
print(dict)
print(dict['name'])
print(dict['born year'])
print(len(dict))
print(type(dict))
