# coding=utf-8

from tkinter import *
import tkinter as tk

window = Tk()

window.title('radio_button')
window.geometry()

var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection():
    l.config(text='you have select ' + var.get())

r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A_', command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B_', command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C_', command=print_selection)
r3.pack()

window.mainloop()