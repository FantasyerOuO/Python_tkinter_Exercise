import tkinter as tk
# 設定一個tkinter
win=tk.Tk()
# 設定視窗大小
win.geometry('500x500')
# 設定視窗最大值和最小值
win.minsize(width=300,height=300)
win.maxsize(width=700,height=700)
# 設定視窗可否縮放
win.resizable(1,1)
# 設定視窗標題
win.title('T1_0423')
# 設定常駐視窗
win.mainloop()