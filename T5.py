
import tkinter as tk
import random as rd
from tkinter import END, messagebox
import pyperclip as pc

win=tk.Tk()

win.geometry('400x400+500+300') # '視窗x視窗y+座標x+座標y'
win.config(bg='#323232')
win.title('教學5實例')

title_lb=tk.Label(text='隨機座標生成器',bg='#323232',fg='skyblue',font=('微軟正黑體 15'))
# obj.config(font="字型 大小")
title_lb.pack()


min_lb=tk.Label(text='Min range',bg='#323232',fg='white',font=('微軟正黑體 10'))
min_lb.pack()
min_en=tk.Entry()
min_en.pack()

max_lb=tk.Label(text='Max range',bg='#323232',fg='white',font=('微軟正黑體 10'))
max_lb.pack()
max_en=tk.Entry()
max_en.pack()

x_lb=tk.Label(text='',bg='#323232',fg='white',font=('微軟正黑體 10'))
x_lb.pack()
y_lb=tk.Label(text='',bg='#323232',fg='white',font=('微軟正黑體 10'))
y_lb.pack()

def rad():
    Copy_btn.config(text='Copy')
    min=int(min_en.get())
    max=int(max_en.get())
    if min<max:
        x_lb.config(text="X:"+str(rd.randint(min,max)))
        y_lb.config(text="Y:"+str(rd.randint(min,max)))
    else:
        messagebox.showwarning('error','min or max error')
        min_en.delete(0,END)
        max_en.delete(0,END)
        x_lb.config(text='')
        y_lb.config(text='')
        
def copy():
    # cget(config get)取得config特定屬性值?
    xy=x_lb.cget("text")+'\n'+y_lb.cget("text")
    pc.copy(xy)
    Copy_btn.config(text='Copied')
        

Generator_btn=tk.Button(text='Generate',command=rad) 
Generator_btn.pack()

Copy_btn=tk.Button(text="Copy",command=copy)
Copy_btn.pack()

win.mainloop()
