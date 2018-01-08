---
title:  流程备忘提醒
date: 2017-09-06 15:22:41
tags: 
      - python
      - 备忘提醒
      - GUI
---

本篇主要是利用python写一个办公室备忘提醒，比如间隔多长时间我需要去处理分配的任务，像这种需求的时候，就可以定时弹出一个windows弹框，提醒自己该去处理什么事情了.

像我本机已经安装了python,直接双击.py文件就可以了；如果想发给没有环境的人的话，那就最好封装成exe文件了.

![](http://7xl4c6.com1.z0.glb.clouddn.com/Fhmonn3-ibpvI6F9oqu6W8H-fBjG)

<!-- more -->

代码如下:

```bash

from tkinter import *
import time

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='   现在已经过了30min，应该去把前天的算法再研究一遍了  ')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

time.sleep(30*60)
		
app = Application()
# 设置窗口标题:
app.master.title('   看我！ 看我！看我！  ')
# 主消息循环:
app.mainloop()

```

PS. 如果是多个任务，直接for循环结合elif也是比较简单的，这边不做重写，本来就是几个小demo，太多代码的话就脱离了小demo的本意，而且如果自己动手的话，这个需求也很简单（大家又不是谁没写过代码一样）.

