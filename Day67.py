#Program to Display Powers of 2 Using Anonymous Function



terms = int(input("Enter number: "))


result = list(map(lambda x: terms ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print(f"{terms} raised to power",i,"is",result[i])
