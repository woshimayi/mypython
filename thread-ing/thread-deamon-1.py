import threading

#定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数
def action(length):
    print(length)
    for arc in range(length):
        #调用 getName() 方法获取当前执行该程序的线程名
        print(threading.current_thread().getName()+" "+str(arc))

#创建线程
thread = threading.Thread(target = action,args =(20,))

#将thread设置为守护线程
thread.daemon = True

#启动线程
thread.start()

#主线程执行如下语句
for i in range(5):
    print(threading.current_thread().getName())