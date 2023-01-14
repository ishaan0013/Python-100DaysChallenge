#local vs global variable
var1=50
print(f"{var1} is a global variable.")

def my_func():
    var1=80
    print(f"{var1} is a local variable.")
    
my_func()

#we can also change a global variable inside a function by global keyword

def second_fnc():
    global var1 
    var1=100
    print(f"Now {var1} is changed globally.")
    
    
second_fnc()