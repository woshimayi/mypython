import threading


#主线程执行如下语句
for i in range(5):
    print(threading.current_thread().getName())


# 定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数
def action(*add):
    for arc in add:
        #调用 getName() 方法获取当前执行该程序的线程名
        print(threading.current_thread().getName() +" "+ arc)

#定义为线程方法传入的参数
my_tuple = ("http://c.biancheng.net/python/",\
            "http://c.biancheng.net/shell/",\
            "http://c.biancheng.net/java/")
#创建线程
thread = threading.Thread(target = action,args =my_tuple)
#启动线程
thread.start()