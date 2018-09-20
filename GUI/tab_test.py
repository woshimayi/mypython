# coding=utf-8

# author: woshidamayi

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext 

win = Tk()
win.title('Python GUI')
win.geometry('400x300')

tabControl = ttk.Notebook()
# =================================================================================================
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tabControl.pack(expand=1, fill='both')
# =================================================================================================
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill='both')
# =================================================================================================
monty = ttk.LabelFrame(tab1, text='Monty Python')
monty.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(monty, text='Enter a name').grid(column=0, row=0, sticky='W')
# =================================================================================================
monty1 = ttk.LabelFrame(tab2, text='Monty C')
monty1.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(monty1, text='Enter a passwd').grid(column=0, row=0, sticky='W')
# =================================================================================================
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty, text='Disabled', variable=chVarDis, state='disabled')
check1.grid(column=0, row=1)
# =================================================================================================
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value+'\n')

spin = Spinbox(monty, value=(0, 50, 100), width=5, bd=8, command=_spin)
spin.grid(column=0, row=2)

spin = Spinbox(monty, value=(0, 50, 100), width=5, bd=8, command=_spin)
spin.grid(column=1, row=2)

# =================================================================================================
class ToolTip(object):
    def __init__(self,widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
    
    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cn, cy = self.widget.bbox('insert')
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT, background = '#ffffe0', relief=tk.SOLID, borderwidth=1, font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)
    
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
        

def createToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
# =================================================================================================

createToolTip(spin, 'This is a Spin control')
# =================================================================================================
scrolW = 30; scrolH = 3
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, row=3, stick='WE', columnspan=3)
# =================================================================================================
createToolTip(scr, 'This is a ScrolledText widget')


# =================================================================================================
# =================================================================================================
tabControl = ttk.Notebook(win)
# =================================================================================================
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
# =================================================================================================
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
# =================================================================================================
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Tab 3")
# =================================================================================================
tabControl.pack(expand=1, fill="both")
# =================================================================================================
tab3 = tk.Frame(tab3, bg='blue')
tab3.pack()
for orangeColor in range(2):
    canvas = tk.Canvas(tab3, width=150, height=80, highlightthickness=0, bg='orange')
    canvas.grid(row=orangeColor, column=orangeColor)
# =================================================================================================
# =================================================================================================


# ====================how to get data from a widget=================
strData = spin.get()
print("spinbox value:" + strData)

nameEntered = ttk.Entered(monty1, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, stick=tk.W)

nameEntered.focus()


win.mainloop()