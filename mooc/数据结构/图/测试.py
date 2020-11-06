def func(lst1):
    s1, s2 = Stack(), Stack()
    for item in lst1:
        s1.push(item)
    lst2 = []
    while not s1.isEmpty():
        for i in range(s1.pop()):
            s2.push(i)
        lst2.append(s2.size())
    return lst2

if __name__ == '__main__':
    print(func([1, 3, 5, 7, 9]))