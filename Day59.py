#decorators
def greetings(fx):
    def mfx(*args, **kwargs):
        print("Hello User")
        fx(*args, **kwargs)
        print("Thank you. visit again")
    return mfx

@greetings
def result(a,b):
    ans=a+b
    print(ans)
    
result(1,2)