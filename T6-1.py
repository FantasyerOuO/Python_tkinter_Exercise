#布局 pack,place(絕對位置), grid(網格布局)
import tkinter as tk
win=tk.Tk()
# win.geometry('200x200')
win.config(bg='#323232')
#grid(row=行(橫))、column=豎(直))

user_lb=tk.Label(text='User')
user_lb.grid(row=0,column=0)
user_lb.config(bg='#323232',fg='skyblue')

 
# pwd_lb=tk.Label(text='Password')
# pwd_lb.grid(row=1,column=0)
# pwd_lb.config(bg='#323232',fg='skyblue')

user_en=tk.Entry(font='微軟正黑體 20')
user_en.grid(row=0,column=1,rowspan=2)

# pwd_en=tk.Entry()
# pwd_en.grid(row=1,column=1)

win.mainloop()

