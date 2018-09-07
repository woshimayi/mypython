# coding=utf-8

from tkinter import *
import tkinter as tk
from tkinter import ttk

win = Tk()
win.title('layout')
win.geometry('400x300')


# ==============================================================
monty = ttk.LabelFrame(win, text='Monty Python')
monty.grid(column=0, row=0)

ttk.Label(monty, text='A Label').grid(column=0, row=1)
ttk.Label(monty, text='Enter a name:').grid(column=0, row=2)

name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=3, sticky=tk.N)
# ==============================================================



# labellsFrom = ttk.LabelFrame(win, text='Label in a Frame')
# labellsFrom.grid(column=0, row=0)

# ttk.Label(labellsFrom, text='Label1').grid(column=0, row=0)
# ttk.Label(labellsFrom, text='Label2').grid(column=1, row=0)
# ttk.Label(labellsFrom, text='Label3').grid(column=2, row=0)

# nameEntered.focus()

win.mainloop()
