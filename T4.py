import tkinter as tk

win=tk.Tk()
win.geometry('400x400')

def ok():
    t=en.get()
    lab.config(text=t)


# label
lab=tk.Label(text='LAB')
lab.config(bg='cyan',fg='pink',font=('',30,'bold'))
lab.config()
lab.pack()

# entry(輸入)
en=tk.Entry()
en.config(width=10)
en.pack()
# en.get(獲取輸入值)


#btn

btn=tk.Button(text='OK')
btn.config(command=ok)
btn.pack()
win.mainloop()
