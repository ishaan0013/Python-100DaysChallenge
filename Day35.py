#else statement with loops
# Python allows the else keyword to be used with the for and while loops
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")