# 网络库
### urllib库 http 协议常用库
### requests 库 http协议常用库
### BeautifulSoup库 xml格式处理库

import  requests  

# get request
url = 'http://httpbin.org/get'
data = {'key':'value', 'abc':'sys'}
res = requests.get(url, data)
# print(res.text)

# post request

# import requests
url1 = 'http://httpbin.org/post'
data1 = {'key':'value', 'abc':'sys'}
res1 = requests.post(url1, data1)
print(res1.json())


