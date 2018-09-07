# coding=utf-8

import tkinter as tk
from tkinter import *
from tkinter import ttk

win = Tk()
win.title('Python GUI')
win.geometry('400x300')

tabControl = ttk.Notebook()
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tabControl.pack(expand=1, fill='both')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill='both')

monty = ttk.LabelFrame(tab1, text='Monty Python')
monty.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(monty, text='Enter a name').grid(column=0, row=0, sticky='W')

monty1 = ttk.LabelFrame(tab2, text='Monty C')
monty1.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(monty1, text='Enter a passwd').grid(column=0, row=0, sticky='W')

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty, text='Disabled', variable=chVarDis, state='disabled')
check1.grid(column=0, row=1)


win.mainloop()