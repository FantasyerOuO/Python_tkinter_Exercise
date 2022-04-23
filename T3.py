#button

import tkinter as tk
win=tk.Tk()
win.geometry('400x400')

# Function功能
def say_hi():
    print('Hi tkinter')

# 新增button
btn=tk.Button(text='Click')

# btn設置(也可以續接在tk.Button裡面)
# btn.config(bg='pink',fg='cyan') 
# btn.config(width=10,height=2)# 寬高依照網格去設定並非像素

# 新增圖片到Butoon上面
# 設定圖片路徑
img=tk.PhotoImage(file='file\circle_50.png')
# 設定btn
btn.config(image=img)

# 功能(Function)
btn.config(command=say_hi)

# 封裝
btn.pack()


win.mainloop()