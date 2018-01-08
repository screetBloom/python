import urllib
import string
#定义要抓取的页面
url = 'http://www.freebuf.com/articles'
#读取要抓取的页面
globalcontent = urllib.urlopen(url).read()
#捕捉文章列表
#这里在源码中查询"<dt><a href="这个字符串
new_inner01_h = globalcontent.find('<dt>a href=')
print (news_inner01_h)
#这里在源码中查询".html"这个字符串
new_inner01_l = globalcontent.find('.html')
print (news_inner01_l)
#这里对文档流进行分片，从查找到的第一篇文章的头部开始，到尾部结束给提取出来
#注意，头部我进行加13，尾部加5，那是因为查找到的指针处于该字符串的开始，如果不做处理那么结果就不是我想要的数据，所以要把指针向前移动
news_inner01 = globalcontent[news_inner01_h+13:news_inner01_l+5]
print (news_inner01)