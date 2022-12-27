#f string 

#old style of formatting a strin:-
sen="Hii I am {} and i am from {}."
name="Ishaan"
country="India"
print(sen.format(name,country))
print(sen.format(country,name))
#or we can use index line
sen1="Hii I am {0} and i am from {1}."
print(sen1.format(name,country))

#New style
sen3=f"I am {name} and I am from {country}"
print(sen3)

