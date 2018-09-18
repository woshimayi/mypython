# coding=utf-8

from tkinter import *
import tkinter as tk
from  tkinter import Menu
from tkinter import messagebox as mBox


win = Tk()
win.title('MenuBar')
win.geometry('300x400')


menuBar = Menu(win)
win.config(menu=menuBar)

def _quit():
    win.quit()
    win.destroy()
    exit()

fileMenu = Menu(menuBar, tearoff=0)  # tearoff 去掉默认的第一个虚线
fileMenu.add_command(label="New")   # file 选项下拉名称
fileMenu.add_command(label="Edit")   # file 选项下拉名称
fileMenu.add_separator() # 添加分割线
fileMenu.add_command(label='Quit', command=_quit)
menuBar.add_cascade(label='File', menu=fileMenu)    #创建菜单栏

def _msgBox():
    # mbox.showinfo('python Message Info Box', 'A Python GUI created')
    # mbox.showwarning('Python message Warning')
    # mbox.showerror('Python sdfsdfsdf error')
    answer = mBox.askyesno("python Message Dual chiise box", 'are you sure you really wish to do this')

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)



win.mainloop()