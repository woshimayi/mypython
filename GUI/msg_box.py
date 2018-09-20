# coding=utf-8

from tkinter import *
import tkinter as tk
from  tkinter import Menu
from tkinter import messagebox as mBox


win = Tk()
win.title('MenuBar')
win.geometry('300x400')
win.iconbitmap(r'.\123.ico')


menuBar = Menu(win)
win.config(menu=menuBar)

def _quit():
    win.quit()
    win.destroy()
    exit()

def _msgBox():
    mBox.showinfo('python Message Info Box', 'A Python GUI created')
    mBox.showwarning('Python message Warning')
    mBox.showerror('Python sdfsdfsdf error')
    answer = mBox.askyesno("python Message Dual chiise box", 'are you sure you really wish to do this')

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)



win.mainloop()