import urllib,urllib.request 
import sys,locale
import re


def getHtml(data):
	url='http://www.tuling123.com/openapi/api'+'?'+data
	req=urllib.request.Request(url)
	res=urllib.request.urlopen(req)
	html = res.read()
	return html.decode('utf-8')
	
def handleHtml(html):
	text = re.findall('{"code":100000,"text":"(.*?)"}',html)
	print (str(text[0]))
	
while True:
	message=input('-->').strip().encode('utf-8')
	if message=='quit':
		sys.exit(1)
	d={'info':message,
	   'key': 'c68cd1f0c25c4d6fbc451805ed93927b'
	}	
	messagel=urllib.parse.urlencode(d)
	html=getHtml(messagel)
	handleHtml(html)

