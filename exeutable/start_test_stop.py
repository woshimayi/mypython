# -*- coding: UTF-8 -*-
import json
import os
import platform
import signal

import psutil

down_thead_num = 20
parse_thread_num = 1
debug_type = 1
adb_save_list = []



def killpid(pid):
    if 'Windows' == platform.system():
        os.kill(pid, -1)
    else:
        os.kill(pid, signal.SIGKILL)


def get_pid_by_name(name, pid_list):
    plist = psutil.process_iter()
    print(name)
    for temp in plist:
        print(temp)
        if temp.name() == name:
            pid_list.append(temp.pid)


def killSpider():
    adb_del_list = []
    get_pid_by_name('Spider_test.exe', adb_del_list)
    print('Spider_test.exe del: ' + str(adb_del_list))
    for pid in adb_save_list:
        for pid_get in adb_del_list:
            if pid_get == pid:
                adb_del_list.remove(pid_get)
    for pid_get in adb_del_list:
        os.system('taskkill /f  /t /PID ' + str(pid_get))
    return True


start_urls = ["http://www.hao123.com/"]


# killSpider()
# for url in start_urls:
#     os.system('Spider_test.exe '+url+' '+str(down_thead_num)+' '+str(parse_thread_num)+' '+str(debug_type))

# def find_procs_by_name(name):
#     "Return a list of processes matching 'name'."
#     ls = []
#     for p in psutil.process_iter(['name']):
#         if p.info['name'] == name:
#             ls.append(p.pid)
#     return ls
#
# ls = []
# ls = find_procs_by_name('Spider_test.exe')
# print(ls)

def json_format(json_data):
    print(json.dumps(json_data, sort_keys="true", indent=4, separators=(",", ":")))

# print(json_format(psutil.net_if_addrs()))
# print(json_format(psutil.net_if_stats()))
print(json_format(psutil.net_connections()))
# print(json_format(psutil.net_io_counters()))


