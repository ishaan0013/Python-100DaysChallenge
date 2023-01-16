#Readline() & writelines()
f = open('text2.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

f = open('myfile2.txt', 'w')
lines = ['How\n', 'Are\n', 'You\n']
f.writelines(lines)
f.close()