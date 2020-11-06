f = open('data.txt')
ls = []
for line in f:
    line = line.replace('\n', '')
    print(line)
    ls.append(line.split(','))

f.close()
print(ls)