# '~!@#$%^&*()_+[]\{}|;:",./<>?'
def getText():
    txt = open('hamlet.txt', 'r').read()
    txt = txt.lower()
    for ch in '~!@#$%^&*()_+[]\{}|;:",./<>?':
        txt = txt.replace(ch, '')
    return txt


hamleTxt = getText()
words = hamleTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
itmes = list(counts.items())
itmes.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word,count=itmes[i]
    print('{}{}'.format(word,count))