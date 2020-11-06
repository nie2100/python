import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def parserPage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\"[\d\w]*\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print('')


def printGoodslist(ilt):
    tplt = "{:8}\t{:8}\t{:16}"
    print(tplt.format('序号', '价格‘，’商品名称'))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = '8i7hvk'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    inforList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parserPage(inforList, html)

        except:
            continue
    printGoodslist(inforList)


main()
