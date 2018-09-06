from tkinter import *

# 3.1 Label
# 说明
# 　　标签
# 用法
# 　　Label(根对象, [属性列表])
# 属性
# text　   要现实的文本
# bg　　  背景颜色
# font　   字体(颜色, 大小)
# width　 控件宽度
# height　控件高度


root  = Tk()
root.title('hello world')
root.geometry('300x200')
l = Label(root, text='是的发送到', bg='green', font=('Arial', 12), width=5, height=2)
l.pack(side=BOTTOM)
root.mainloop()