# coding=utf-8

# 3.7 Scrollbar
# 说明
# 　　在屏幕上创建一块矩形区域,多作为容器来布局窗体
# 用法
# 　　Frame(根对象, [属性列表]), 最长用的用法是和别的控件一起使用.



from tkinter import *

root = Tk()
root.title('scrollbar')
root.geometry()

def print_item(event):
    print(lb.curselection())

var = StringVar()
lb = Listbox(root, height=5, selectmode=BROWSE, listvariable = var)
lb.bind('<ButtonRelease-1>', print_item)

# list_item =[1,2,3,4,5,6,7,8,9,0]

# for item in list_item:
#     lb.insert(END, item)

# scrl = Scrollbar(root)
# scrl.pack(side=RIGHT, fill=Y)

lb.configure(yscrollcommand = scrl.set)
lb.pack(side=LEFT, fill=BOTH)

# scrl['command'] = lb.yview

root.mainloop()