# ICON、顏色、透明度、置頂
from tkinter  import *  
win=Tk()

# ICON
win.iconbitmap('file\circle.ico')

# 顏色
win.config(bg='cyan')

# 透明度
win.attributes("-alpha",0.5) # 1~0 1=100% 0=0%

#置頂
win.attributes('-topmost',1) # 1=True , 0 =False

win.mainloop()

