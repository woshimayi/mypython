#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: list_test.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/6/16 19:48
 * @LastEditors: sueRimn
 * @LastEditTime: 2022/6/16 19:48
 * @Descripttion: 
'''

if __name__ == '__main__':
    L = ['acsd2', 'cat', 'ceventd', 'consoled', 'date:2022-06-16_19:47:53,', 'dbus-daemon', 'debug_monitor', 'dhcp6s', 'dhcpc', 'dhcpd', 'dnsproxy', 'eapd', 'gwd', 'hbusdaemon', 'hghal', 'hghttpd', 'hlogd', 'hostapd', 'init', 'mcpd', 'mdmd', 'miscd', 'natived', 'omcid', 'openl2tpd', 'osgid', 'portLoopDetect', 'radvd', 'rastatus6', 'sh', 'showmem', 'smd', 'sntp', 'ssk', 'ssk_ty', 'telnetd', 'toad', 'tr69c', 'tydaemon', 'wand', 'wlevt2', 'wlmngr2']
    K = ['acsd2', 'cat', 'consoled', 'date:2022-06-16_19:47:53,', 'dbus-daemon', 'debug_monitor', 'dhcp6s', 'dhcpc', 'dhcpd', 'dnsproxy', 'eapd', 'gwd', 'hbusdaemon', 'hghal', 'hghttpd', 'hlogd', 'hostapd', 'init', 'mcpd', 'mdmd', 'miscd', 'natived', 'omcid', 'openl2tpd', 'osgid', 'portLoopDetect', 'radvd', 'rastatus6', 'sh', 'showmem', 'smd', 'sntp', 'ssk', 'ssk_ty', 'telnetd', 'toad', 'tr69c', 'tydaemon', 'wand', 'wlevt2', 'wlssk_ty', 'wps_pbcd']

    # if len(L)  len(K):
    print(list(set(L) - set(K)))
    M = list(set(L) - set(K))
    # else:
    print(list(set(K) - set(L)))
    N = list(set(K) - set(L))
    # if len(M):
    #
    # elif len(N):

    # print(set(L)|set(K))

    # M = list(set(L) | set(K))
    # print('M', M)
    # print(set(M) - set(K))
    # print(list(set(K) - set(M)))

    # L.extend(K)
    # print(L, len(L))
    # L = list(set(L))
    # print('4', L)
    # print(L.sort())
    print('Hello world')