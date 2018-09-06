# coding=utf-8

# 3.3 Entry
# 说明
# 　　创建单行文本框
# 用法
# 　　创建:lb =Entry(根对象, [属性列表])
# 　　绑定变量 var=StringVar()    lb=Entry(根对象, textvariable = var)
# 　　获取文本框中的值   var.get()
# 　　设置文本框中的值   var.set(item1)



from tkinter import *

root = Tk()
root.title('hello world')
root.geometry()
var = StringVar()
e = Entry(root, textvariable = var)
var.set('hello')
print(var.get())
e.pack()
root.mainloop()


