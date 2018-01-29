---
title: python爬虫由浅入深
date: 2017-09-05 14:46:56
tags: 
      - python
      - 爬虫
    
---

本篇主要展示自己闲暇之余写的python爬虫，比如几个小爬虫案例研究,简单入门，代码扩展中.每天也都有着自己的工作，无聊就写点python，慢慢扩展


![](http://img.mukewang.com/57466ffc00015e2f06000338-590-330.jpg)

<!-- more -->

PS. 所有案例都基于python版本 3.x

基于最新版本，如果还在用2.x，没有大的需求的话，换成3.x，2.x的代码都是可以迁移的，不要怕

### 实例1：爬取baidu首页

![](http://7xl4c6.com1.z0.glb.clouddn.com/Fh9DT6UGI5t4nDQBylJu9J-XuH3r)


代码如下:
```bash
import urllib.request
 
#网址
url = "https://www.baidu.com/"
 
#请求
request = urllib.request.Request(url)
 
#爬取结果
response = urllib.request.urlopen(request)
 
data = response.read()
 
#设置解码方式
data = data.decode('utf-8')
 
#打印结果
print(data)
 
#打印爬取网页的各类信息
 
print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())

```


### 实例2：爬取youdao和百度的翻译功能来翻译自己输入的句子

主要是有时候一直需要打开一个chrome的tab页去翻译觉得很麻烦，就爬了一下翻译功能，自己用的话直接再添加一点东西直接在本地运行，对自己也比较方便.

![](http://7xl4c6.com1.z0.glb.clouddn.com/FpAWXSS-2S8kLRJvY9AzCP2gqy1q)


```bash

import urllib.request  
import urllib.parse  
import json  
  
  
content=input("请输入需要翻译的内容:\n")  
  
  
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'  
data={}  
data['type']='AUTO'  
data['i']=content  
data['doctype']='json'  
data['xmlVersion']='1.8'  
data['keyfrom']='fanyi.web'  
data['ue']='UTF-8'  
data['action']='FY_BY_CLICKBUTTTON'  
data['typoResult']='true'  
  
data=urllib.parse.urlencode(data).encode('utf-8')  
  
response=urllib.request.urlopen(url,data)  
html=response.read().decode('utf-8')  
  
target=json.loads(html)  
print('翻译结果为：%s' % (target['translateResult'][0][0]['tgt']))

```


###  爬取斗鱼上的直播图片

这张图主要是为了展示下面提供的源代码中的16、17行:
```bash
 temp = valueimage[0].split(':')[2]
 temp = "https:"+temp
```
这张如图展示的是我们处理之后得到的urlvalueimage,再对它处理一下就能拿到我们想要的url了,也就是这里16、17行的出现在这里的意义.


这张图展示的是下载图片的过程.

![数据格式](http://7xl4c6.com1.z0.glb.clouddn.com/FvdMuYaI14gG0qcH96GSUSPFS87D)



![下载过程](http://7xl4c6.com1.z0.glb.clouddn.com/FmyTYbVXgt5aWk0aSs8I46YiJ6ki)

最终，爬到的部分数据(你可以选择一直跑，我这里就取一次数据)：

![读取到的图片](http://7xl4c6.com1.z0.glb.clouddn.com/FpW7tF8fjRtT_rZte3VQ5gZ4yuET)


代码如下：

```bash  


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


```

如果你对某个女主播感兴趣，搜索一下如何截取视频（或者直接拉视频），把爬虫放在服务器上天天跑，那就比较刺激了.



### 爬火车订票单号

暂时还没开始写，一方面是公司在做这个，有点顾忌,另外一方面主要是没找到一个特别好的样例来改

这个跳过，万一出现问题，被人举报，我可能会被辞退，还是算了

## 正式开始刺激的


### 爬美女图片(如果想爬小黄图的话，切换网址)



有没有什么时候觉得浏览黄图太麻烦了，万一被删除了也麻烦，不如一次爬下来，以后慢慢欣赏 -_- 
PS.首先声明我是从来不做这种事情的，如果down了代码的话，请注意身体,声明我身体很好，也不做这种事


其实说实话，很多小黄图网站我试了一下，都挺好爬的，因为这类网站频繁更换等原因，我目前测试了1个“你懂得”网站，既没有ip封锁也没有反爬虫,所以我发现爬小黄图也是爬虫的一个很好的应用场景

加入有上述问题，解决办法：
&emsp;&emsp;&emsp;&emsp;1.ip代理
&emsp;&emsp;&emsp;&emsp;2.Anti-Anti-Spider,详情可以github"luyishisi"

代码已经给出了详细的说明，这里不做多余的说明
这里主要是想把爬虫做的刺激点,我这里是爬10页的量，如果量不够，改代码第60行的page=10,自己修改页数

这里只展示一部分，差不多爬了有 200张
![](http://7xl4c6.com1.z0.glb.clouddn.com/Flu5MVTO1SzKOwsSDFEDV2ME4yY4)

源代码如下:
```bash

import urllib.request  
import os  
import time  
  
# 打开URL，返回HTML信息  
def open_url(url):  
    # 根据当前URL创建请求包  
    req = urllib.request.Request(url)  
    # 添加头信息，伪装成浏览器访问  
    req.add_header('User-Agent',  
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')  
    # 发起请求  
    response = urllib.request.urlopen(req)  
    # 返回请求到的HTML信息  
    return response.read()  
  
# 查找URL中的下一页页码  
def get_page(url):  
    # 请求网页，并解码  
    html=open_url(url).decode('utf-8')  
    # 在html页面中找页码  
    a=html.find('current-comment-page')+23  
    b=html.find(']',a)  
    # 返回页码  
    return html[a:b]  
  
# 查找当前页面所有图片的URL  
def find_imgs(url):  
    # 请求网页  
    html=open_url(url).decode('utf-8')  
    img_addrs=[]  
    # 找图片  
    a = html.find('img src=')  
    #不带停，如果没找到则退出循环  
    while a != -1:  
        # 以a的位置为起点，找以jpg结尾的图片  
        b = html.find('.jpg',a, a+255)  
        # 如果找到就添加到图片列表中  
        if b != -1:  
            img_addrs.append(html[a+9:b+4])  
        # 否则偏移下标  
        else:  
            b=a+9  
        # 继续找  
        a=html.find('img src=',b)  
    return img_addrs  
  
# 保存图片  
def save_imgs(img_addrs):  
    for each in img_addrs:  
        print('download image:%s'%each)  
        filename=each.split('/')[-1]  
        with open(filename,'wb') as f:  
            img=open_url("http:"+each)  
            f.write(img)  
  
# 下载图片  
# folder 文件夹前缀名  
# pages 爬多少页的资源，默认只爬10页
# 文件夹默认在当前路径下，创建 ‘girl’+  文件夹  
def download_mm(folder='girl',pages=10):  
    folder+= str(time.time())  
    # 创建文件夹  
    os.mkdir(folder)  
    # 将脚本的工作环境移动到创建的文件夹下  
    os.chdir(folder)  
  
    # 本次脚本要爬的网站  
    url='http://jandan.net/ooxx/'  
    # 获得当前页面的页码  
    page_num=int(get_page(url))  
    for i in range(pages):  
        page_num -= i  
        # 建立新的爬虫页  
        page_url=url+'page-'+str(page_num-1)+'#comments'  
        # 爬完当前页面下所有图片  
        img_addrs=find_imgs(page_url)  
        # 将爬到的页面保存起来  
        save_imgs(img_addrs)  
  
if __name__ == '__main__':  
    download_mm() 

```



### 利用爬虫做个中文机器人

心血来潮做的一个小中文机器人,利用的其实还是网页抓取,核心技术由图灵机器人提供

测试场景如下:

![](http://7xl4c6.com1.z0.glb.clouddn.com/FiumljGDdXcluaFrQ-2D9ZSMe-K9)


源代码如下:

```bash

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
	   'key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	}	
	messagel=urllib.parse.urlencode(d)
	html=getHtml(messagel)
	handleHtml(html)



```



进一步代码后续展示

拓展中......
