#string operations
#stringd are immutabale

a = 'isHaAn bhaRdwAj'
#1
print(len(a)) #print length of str
#2
print(a.upper()) #convert str in uppercase
#3
print(a.lower()) #convert str in lowercase
#4
print(a.capitalize()) #this function capitalize first letter of str and all other to lowercase
#5 
print(a.center(50)) #put space before str
#6
print(a.rstrip('j')) #cuts off the char from ending of str
#7
# print(a.index('q')) #index & find functions are same, The only difference is that find return -1 if the char is not in the str
#8
print(a.find('q'))
#9
print(a.replace('isHaAn','shanu')) #this will not effect the original str
print (a)
#10
print(a.isalnum()) #Return True if the string is an alpha-numeric string, False otherwise.A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.
#11
print(a.isalpha()) #Return True if the string is an alphabetic string, False otherwise.A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.
#12
print(a.title()) #words start with uppercased characters and all remaining cased characters have lower case.
#13
print(a.swapcase()) #Convert uppercase characters to lowercase and lowercase characters to uppercase.
#14
print(a.istitle()) #Return True if the string is a title-cased string, False otherwise.