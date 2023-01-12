#os function in Python
import os
if(not os.path.exists("46 day reference")):
    os.mkdir("46 day reference")
if(not os.path.exists("46 day reference/By os")):
    os.mkdir("46 day reference/By os")
os.getcwd() #this shows the current directory
print(os.listdir("46 day reference")) #this will list all the directory 
os.rename("46 day reference/By os","46 day reference/Very nice")#this will rename a current directory