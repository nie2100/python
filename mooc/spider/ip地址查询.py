import requests

ip = {'ip': '61.135.169.121'}

header = {'user-agent': 'Mozilla/5.0'}

url = 'http://www.ip138.com/ips138.asp'

try:
    r = requests.get(url, params=ip)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)

except:
    print('爬取错误')
