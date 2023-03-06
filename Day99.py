import re

name = "HelloiamIshaanbharDwAj !, 123"

uppercase_characters = re.findall(r"[A-Z]", name)
lowercase_characters = re.findall(r"[a-z]", name)
numerical_characters = re.findall(r"[0-9]", name)
special_characters = re.findall(r"[, .!?]", name)

print("The no. of uppercase characters is", len(uppercase_characters))
print("The no. of lowercase characters is", len(lowercase_characters))
print("The no. of numerical characters is", len(numerical_characters))
print("The no. of special characters is", len(special_characters))
