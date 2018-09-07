#coding=utf-8

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import tkinter as tk

win = Tk()
win.title('sizeofable')
win.resizable(1,1) # 括号内数字随便写
win.geometry('400x500')

# ttk.Label(win, text='A Lable').grid(column=0, row=0)
# ttk.Label(win, text='B Lable').grid(column=0, row=1)


aLabel = ttk.Label(win, text='A Lable')
aLabel.grid(column=0, row=0)
# ttk.Label(win, text='B Lable').grid(column=1, row=0)

def clickMe():
    # action.configure(state='disabled') # 点击之后变为灰色
    action.configure(text='chose:' + name.get() + ' ' +  ' ' + numberChose.get()) # 点击之后变为灰色
    aLabel.configure(background='red', text=name.get())

# 按钮
action = ttk.Button(win, text='Click Me', command=clickMe)
action.grid(column=0, row=1)

# 文本框
name = tk.StringVar()
nameEntered = ttk.Entry(win , width=12, textvariable=name)
nameEntered.focus()  # 确保光标在读入文本框中
nameEntered.grid(column=1, row=1)

# 选择框
ttk.Label(win, text='Choose a number:').grid(column=1, row=0)
number = tk.StringVar()
numberChose = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChose['values'] = (1,2,3,42, 100)
numberChose.grid(column=2, row=1)
numberChose.current(0)

# create three checkbox
checkvardis = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disabled', variable=checkvardis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

checkvardis1 = tk.IntVar()
check2 = tk.Checkbutton(win, text='Enabled', variable=checkvardis1)
check2.select()
check2.grid(column=1, row=4, sticky=tk.W)

checkvardis2 = tk.IntVar()
check3 = tk.Checkbutton(win, text='Uncheck', variable=checkvardis2)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)


# scroll 编辑框
scrolW = 50
scrolH = 5
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
# scr.grid(column=0, sticky='WE', columnspan=3) # 靠近边框
scr.grid(column=0, columnspan=3)   #  columnspan 占据列数

colores = ['Blue', 'Gold', 'Red']
# create three radiobutton
radVar = tk.IntVar()
radVar.set(99)

def radCall():
    radSel = radVar.get()
    if radSel == 0: win.configure(background=colores[0])
    elif radSel == 1: win.configure(background=colores[1])
    elif radSel == 2: win.configure(background=colores[2])


for col in  range(3):
    curRad = 'Rad' + str(col)
    curRad = tk.Radiobutton(win, text=colores[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=3, sticky=tk.S)

# ==========================================================
labellsFrom = ttk.LabelFrame(win, text='Label in a Frame')
labellsFrom.grid(column=0, row=7, padx=10, pady=10, sticky=tk.E) # pad 周围ｓｐａｃｅ的宽度

ttk.Label(labellsFrom, text='Label1').grid(column=0, row=0)
ttk.Label(labellsFrom, text='Label2').grid(column=0, row=1)
ttk.Label(labellsFrom, text='Label3').grid(column=0, row=2)

# 添加space
for child in labellsFrom.winfo_children():
    child.grid_configure(padx=0, pady=10)  #宽度和高度
# ===========================================================









































































win.mainloop()

