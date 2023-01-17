#A program to print digits of a number into words
#Input:-     output:-
#1221        one two two one
dic = {0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
a = int(input("Enter the number: "))
b = str(a)
for i in range(len(b)):
    c = int(b[i])
    print(dic[c],end=" ")