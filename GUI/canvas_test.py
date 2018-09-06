# coding=utf-8

from tkinter import *
import tkinter as tk

window = Tk()
window.title('canvas')
window.geometry('400x500')

canvas = tk.Canvas(window, bg='green', height=200, width=500)

image_file = tk.PhotoImage(file='pic.gif')

image = canvas.create_image(250, 50, image=image_file)

x0, y0, x1, y1 = 100, 100, 150, 150

line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)
oval = canvas.create_oval(x0+120, y0+50, x1+50, y1+50, fill='yellow')
arc = canvas.create_arc(x0, y0+50, x1+50, y1+50, start=0, extent=180)
rect = canvas.create_rectangle(330, 30, 330+20, 50)
canvas.pack()

def moveit():
    canvas.move(rect, 2, 2)

b = tk.Button(window, text='move item', command=moveit).pack()



window.mainloop()
    