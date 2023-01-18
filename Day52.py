# #lambda functions

def add(num):
    return num+num

print(add(10))
# #This the the normal method for a function


ad= lambda x: x+x
print(ad(10))
#this is lambda function
# #it is used for writing small functions




def app(fx,value):
    return value + fx(value)

print(app(lambda x: x+x,2))
#we can also use it to pass function in another function