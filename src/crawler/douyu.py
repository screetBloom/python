#coding=utf-8

#import module
import urllib
import urllib.request
import re  


j=1
imageline="https://staticlive.douyucdn.cn/storage/webpic_resources/upload/slide/2017/0904/201709041558412747.jpg"

urllib.request.urlretrieve(imageline ,'D:\\python\\temp\\imgs\\%d.jpg'%j)

#f = urllib.request.urlopen("http://douyu.com")
#获取文件的全部内容   
#value = f.read()

#value = value.decode('utf-8')


#打印出文件的全部内容
#print(value)

#获取相应匹配字符串,并以列表的形式进行返回
#src="https://rpic.douyucdn.cn/roomCover/2017/03/02/417441e4948021aa1de92a820abe8ece.png"
#imagelist = re.findall(r'src="(.*?\.(jpg|png))"',value)


#j=0
#for valueimage in imagelist:
    #imageline = valueimage[0]
    #print('正在下载 %s'%imageline )
    #urllib.request.urlretrieve(imageline ,'D:\\download\\%d.jpg'%j)
    #j+=1