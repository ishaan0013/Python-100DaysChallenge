#A program to code & decode a secret code_Word
# code:
#     if the string is less than 3 then just reverse it
#     otherwise take first letter of string and put it in last and then
#     add 3 random letter in front and last of string
# decode:
#     if the string is less than 3 then just reverse it
#     otherwise cut first 3 and last 3 letters and then put that last word in front 
import random
import string

def code():
    inp=input("Enter string to code it:")
    if(len(inp)<3):
        print("Your code is: ",inp[::-1])
    else:
        a=inp[0]
        inp2=inp[1:]
        inp2=inp2+a
        start= ""
        last=""
        for i in range(0,3):
            start=start+(random.choice(string.ascii_letters))
        for i in range(0,3):
            last=last+(random.choice(string.ascii_letters))
        inp2=start+inp2+last
        print("Your code is "+inp2)
        
def decode():
    inp=input("Enter the code to decode it:")
    if(len(inp)>=3):
        lent=len(inp)
        inp2=inp[3:len(inp)-3]
        a=len(inp2)
        char=inp2[a-1]
        inp2=inp2[:len(inp2)-1]
        char=char+inp2
        print("Your decoded word is: ",char)
    else:
        print("Your decode is: ",inp[::-1])

ques=int(input("Press 1: Code \n      2: Decode "))
if(ques==1):
    code()
elif(ques==2):
    decode()
else:
    print("Please enter 1 or 2.")
    

        
    