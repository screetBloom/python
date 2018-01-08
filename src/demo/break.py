
import time
import webbrowser

total_break = 3
count_break = 0

print("This program started on "+time.ctime())
while(count_break < total_break):
  time.sleep(2*60*60)
  webbrowser.open("http://music.163.com/song/431794103/?userid=390661347")
  count_break = count_break + 1 



