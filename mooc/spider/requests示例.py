import requests

url = 'http://python123.io/ws/demo.html'

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    with open('demo.html', 'wb') as f:
        f.write(r.content)
        f.close()
except:
    print('爬取异常')
