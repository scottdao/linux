# 网络库
# urllib库 http 协议常用库
# requests 库 http协议常用库
# BeautifulSoup库 xml格式处理库

from bs4 import BeautifulSoup
import socket
import urllib
from urllib import request
from urllib import parse

data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf-8')

url = 'http://www.baidu.com'

response = request.urlopen('http://httpbin.org/post', data=data)

# jg = response.read().decode('utf-8')
jg = response.read().decode('utf-8')
# print(jg)


try:
    res2 = request.urlopen('http://httpbin.org/get', timeout=1)
    jg2 = res2.read()
    soup = BeautifulSoup(jg2, 'lxml')
#    print(jg2)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('timeout')
