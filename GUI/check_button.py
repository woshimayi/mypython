# coding=utf-8

from tkinter import *
import tkinter as tk

window = Tk()
window.title('check button')
window.geometry('400x500')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_select():
    if   (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love python')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I love not love either')
    else:
        l.config(text='I love both')

var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_select)
c1.pack()

c2 = tk.Checkbutton(window, text='C++',    variable=var2, onvalue=1, offvalue=0, command=print_select)
c2.pack()

window.mainloop()