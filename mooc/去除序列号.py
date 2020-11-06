import chardet
f = open('新郑食品安全宣传标语.txt', 'rb',encoding='GB2312')

for item in t:
    print(item.decode('utf-8'))