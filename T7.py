import tkinter as tk
win=tk.Tk()
win.geometry('200x200+400+400')
win.config(bg='#323232')

#pack()的先後順序會讓中心線變動，導致布局的結果也會有變動的可能
btn=tk.Button(text='Button')
btn.pack(side=tk.TOP)
btn=tk.Button(text='Button')
btn.pack(side=tk.BOTTOM)
btn=tk.Button(text='Button')
btn.pack(side=tk.LEFT)
btn=tk.Button(text='Button')
btn.pack(side=tk.RIGHT)

win.mainloop()
