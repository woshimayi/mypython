# coding=utf-8

# 3.6 Listbox
# 说明
# 　　列表控件,可以含有一个或多个文本想,可单选也可多选
# 用法
# 　　创建:lb = ListBox(根对象, [属性列表])
# 　　绑定变量 var=StringVar()    lb=ListBox(根对象, listvariable = var)
# 　　得到列表中的所有值            var.get()
# 　　设置列表中的所有值            var.set((item1, item2, .....))
# 　　添加:                       lb.insert(item)
# 　　删除:                       lb.delete(item,...)
# 　　绑定事件 lb.bind('<ButtonRelease-1>', 函数)
# 　　获得所选中的选项 lbl.get(lb.curselection())
# 属性
# 　　selectmode可以为BROWSE MULTIPL SINGLE




from tkinter import *

root = Tk()
root.title('list')
root.geometry()

def print_item(event):
    print(lb.get(lb.curselection()))

var = StringVar()
lb = Listbox(root, listvariable = var)
var.set(('a', 'ab', 'c', 'd')) # 重新设置，这时控件内容就变成var的内容了
lb.bind('<ButtonRelease-1>', print_item)
lb.pack(side=RIGHT)

# list_item = [1,2,3,4]  # 空间的内容为1 2 3 4
# for item in list_item:
#     lb.insert(END, item)

# lb.delete(2,4)   # 此时的空间内容为 1 3

def print_item1(event):
    print(ld.get(ld.curselection()))

var1 = StringVar()
ld = Listbox(root, listvariable = var1)
var1.set(('1', '2', '3', '4')) # 重新设置，这时控件内容就变成var的内容了
# print(var.get())
ld.bind('<ButtonRelease-1>', print_item1)
ld.pack(side=LEFT)

root.mainloop()