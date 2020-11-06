import requests
import os

kv = {'user-agent': 'Mozilla/5.0'}
search = {'wd': '光明'}
pic = 'pick'
url = "https://i.guancha.cn/news/2018/12/11/20181211202633110.jpg"
path = pic + '/'+url.split('/')[-1]
try:
    if not os.path.exists(pic):
        os.mkdir(pic)
    if not os.path.exists(path):
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
except:
    print('爬取失败，请检查代码')
