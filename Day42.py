#enumerate function
#it takes the given input as a collection or tuples and returns it as an enumerate object
#Example:

marks_out_of_100=[12,23,45,13,99,100,64,67]
# index=0
# for i in range (0,len(marks_out_of_100)):
#     if(index==4):
#         print("abcd")
#     index +=1
#this is normal method

for index,i in enumerate(marks_out_of_100):
    print(index,i)
#by this we get all index and its values