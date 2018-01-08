#coding=utf-8

#import module
import urllib.request
import re  
f = urllib.request.urlopen("http://douyu.com")

value = f.read()

value = value.decode('utf-8')

imagelist = re.findall(r'src="(.*?\.(jpg|png))"',value)

j=0
for valueimage in imagelist:
    temp = valueimage[0].split(':')[2]
    temp = "https:"+temp
    print('正在下载 %s'%temp )
    urllib.request.urlretrieve(temp ,'D:\\python\\temp\\imgs\\%d.jpg'%j)
    j+=1


