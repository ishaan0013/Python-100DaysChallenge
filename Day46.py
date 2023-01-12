#os module in Python
#this is a very vast module, some of its functions are:
import os
if(not os.path.exists("46 day reference")):
    os.mkdir("46 day reference")
if(not os.path.exists("46 day reference/By os")):
    os.mkdir("46 day reference/By os")
os.getcwd() #this shows the current directory
# print(os.listdir("46 day reference")) #this will list all the directory 
# os.rename("46 day reference/By os","46 day reference/Very nice")#this will rename a current directory


# os.chdir("C:\IISHHAANN\Python 100Days challenge\46 day reference\By os")
path='C:/IISHHAANN/Python 100Days challenge/46 day reference'
os.chdir(path)
print(os.getcwd())
with open("demo.txt","w") as fp:
    pass