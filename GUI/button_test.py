# coding=utf-8

# 3.5 Button
# 说明
# 　　创建按钮
# 用法
# 　　Button(根对象, [属性列表])

from tkinter import *
import tkinter as tk
root = Tk()

root.title('hello world')
root.geometry()
# =====================================================
# i = 0
# def printfhello():
#     global i
#     i = i+1
#     # print(i)
#     t.insert('3.0', i)

# t = Text()
# t.pack()
# =====================================================
i = 0
def printfhello():
    global i
    i = i+1
    # print(i)
    var.set(i)

var = tk.StringVar()
l = Label(root, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=4, height=2)
l.pack()

Button(root, text='press', command=printfhello).pack()
root.mainloop()