#7个主要方法

    requests.request()          构造一个请求，支撑以下方法
    requests.get()              获取HTML网页的主要方法，对应于HTTP的GET
    requests.head()             获取HTML网页头信息的方法，对应HTTP的HEAD
    requests.post()             向HTML网页提交POST请求的方法，对应HTTP的POST
    requests.put()              向HTML网页提交PUT请求的方法，对应HTTP的PUT
    requests.patch()            向HTML网页提交局部修改请求，对应HTTP的PATCH
    requests.delete()           向HTML网页提交删除请求，对应HTTP的DELETE

#Response对象的属性

    r.status_code               HTTP请求的返回状态，200表示连接成功，404表示失败
    r.text                      HTTP相应内容的字符串形式，即，url对应的页面内容
    r.encoding                  从HTTP header中猜测的响应内容编码方式
    r.apparent_encoding         从内容中分析出的响应内容编码方式（备选编码方式）
    r.content                   HTTP响应内容的二进制形式

#理解Requests库的异常

    requests.ConnectionError    网络连接异常，如DNS查询失败、拒绝连接等
    requests.HTTPError          HTTP错误异常
    requests.URLRequired        URL缺失异常
    requests.TooManyRedirects   超过最大定向次数，产生重定向异常
    requests.ConnectTimeout     连接远程服务器超时异常
    requests.Timeout            请求URL超时，产生超时异常
    r.raise_for_status()        如果不是200，产生异常requests.HTTPError
    
#requests.request(method,url,**kwargs):

###method                      请求方式，对应get/put/post等7种
    
        r=requests.request('GET',url,**kwargs)
        r=requests.request('HEAD',url,**kwargs)
        r=requests.request('POST',url,**kwargs)
        r=requests.request('PUT',url,**kwargs)
        r=requests.request('PATCH',url,**kwargs)
        r=requests.request('delete',url,**kwargs)
        r=requests.request('OPTIONS',url,**kwargs)
        
###url                         拟获取页面的url链接

###**kwargs                    控制访问的参数，共13个
    
        params:             字典或字节序列，作为参数增加到url中
        data:               字典、字节序列或文件对象，作为Request的内容
        json:               JSON格式的书记，作为Request的内容
        headers:            字典，HTTP定制头
        cookies:            字典或CookieJar，Request中的cookie
        auth:               元组，支持HTTP认证功能
        file:               字典类型，传输文件
        timeout:            设定超时时间，秒为单位
        proxies:            字典类型，设定访问代理服务器，可以增加登录认证
        allow_redirects:    True/False,默认为True，重定向开关
        stream:             True/False,默认为True，获取内容立即下载开关
        verify:             True/False,默认为True，认证SSL证书开关
        cert:               本地SSL证书路径

