#coding=utf-8

from tkinter import *
import tkinter as tk

window = Tk()
window.title('scale')
window.geometry('300x300')

l = tk.Label(window, bg='green', fg='white', text='empty')
l.pack()

def print_select(v):
    l.config(text='you have select' + v)
s = tk.Scale(window, label='W', 
                    from_=0, 
                    to=10, 
                    resolution=0.1,
                    orient=tk.HORIZONTAL, 
                    length=500,
                    showvalue=0, 
                    tickinterval=1, 
                    command=print_select)
s.pack()


def print_select1(v):
    l1.config(text='you have select' + v)

l1 = tk.Label(window, bg='green', fg='white', text='empty')
l1.pack(side=RIGHT)
s1 = tk.Scale(window, label='H', 
                    from_=0, 
                    to=10, 
                    resolution=0.1,
                    # orient=tk.HORIZONTAL, 
                    length=500,
                    showvalue=0, 
                    tickinterval=1, 
                    command=print_select1)
s1.pack(side=RIGHT)


window.mainloop()