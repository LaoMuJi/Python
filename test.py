import re

a = b'GET /index.html HTTP/1.1\r\nHost: 127.0.0.1:8888\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nDNT: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\n'
b = a.splitlines()

c = b[0].decode()
print(c)
re = re.match(r'[^/]+(/[^ ]*)', c).group(1)
print(re)

