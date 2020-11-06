import requests

from bs4 import BeautifulSoup
import traceback
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getStockList(lst, stockURL):
    return ''


def getstockinfo(lst, stockURL, fpatch):
    return ""


if __name__ == '__main__':
    stock_list_url = 'http://quote.eastmoney.com/stocklist.htm'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = '/home/gm/Desktop/折腾/python/untitled/mooc/spider/股票信息'
    slist = []
    getStockList(slist, stock_list_url)
    getstockinfo(slist, stock_info_url, output_file)
