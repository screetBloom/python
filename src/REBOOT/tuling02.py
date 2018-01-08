import urllib,urllib.request 
import sys
import json

reload(sys) 
sys.setdefaultencoding('utf-8') 

API_KEY = 'c68cd1f0c25c4d6fbc451805ed93927b'
raw_TULINURL = "http://www.tuling123.com/openapi/api?key=%s&info=" % API_KEY

def result():
    for i in range(1,100):
        queryStr = raw_input("我:".decode('utf-8'))
        TULINURL = "%s%s" % (raw_TULINURL,urllib.request.quote(queryStr))
        req = urllib.request.Request(url=TULINURL)
        result = urllib.request.urlopen(req).read()
        hjson=json.loads(result)
        length=len(hjson.keys())
        content=hjson['text']

        if length==3:
            return 'robots:' +content+hjson['url']
        elif length==2:
            return 'robots:' +content

if __name__=='__main__':
    print ("你好，请输入内容:".decode('utf-8'))
    contents=result()
    print (contents)