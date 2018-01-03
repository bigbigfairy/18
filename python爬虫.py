import urllib2
url = 'http://wuxi.baixing.com/gongzuo/?afo=1eD'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
req =urllib2.Request(url, headers=headers)
response= urllib2.urlopen(req)
with open('D:/test.html','wb') as f:
    f.write(response.read())
