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