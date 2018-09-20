# coding=utf-8

# author: woshidamayi

from tkinter import *
import tkinter as tk

win = Tk()
# ==================================================================
strData = tk.StringVar()
strData.set('Hello StringVar')
varData = strData.get()
print(varData)
# ==================================================================

print(tk.IntVar())
print(tk.DoubleVar())
print(tk.BooleanVar())


intData = tk.IntVar()
print(intData)
print(intData.get())

# ====================how to get data from a widget=================
