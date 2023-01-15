#basic File IO

f=open("demo file.txt","w")
f.write("Hello")
f.close()
# #this will create a file and write the content in it

f=open("demo file.txt","a")
f.write(" How are you?")
f.close()
# #this will append the content in the last of the file

f=open("demo file.txt","r")
text=f.read()
print(text)
f.close()
#this will read the file
