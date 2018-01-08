---
title: 定时听歌休息
date: 2017-09-06 14:39:41
tags: 
      - python
      - 定时休息
      
---

python上手第二天.

本篇主要是利用python写一个提醒我们休息的小demo，每隔2个小时，调用默认浏览器自动打开网易云分享出来的一首我喜欢的钢琴纯音乐《如果爱有天意》.
平时我在公司时也可能会将代码稍作修改，来提醒自己做一些特定的事情.想制作exe的话，自己搜索一下，也很简单.

<!-- more -->

![](https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3174607735,3028585932&fm=27&gp=0.jpg)

代码如下：

```bash
import time
import webbrowser

total_break = 3
count_break = 0

print("This program started on "+time.ctime())
while(count_break < total_break):
  time.sleep(2*60*60)
  webbrowser.open("http://music.163.com/song/431794103/?userid=390661347")
  count_break = count_break + 1 


```
