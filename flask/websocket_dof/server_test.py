#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: deamoncao100@gmail.com
@software: garner
@file: server_test.py
@time: 22/10/30 15:20
@desc:
'''

import asyncio
import websockets
import websockets_routes

# 初始化一个router对象
router = websockets_routes.Router()


@router.route("/light/{status}")  # 添加router的route装饰器，它会路由uri。
async def light_status(websocket, path):
    async for message in websocket:
        print("got a message:{}".format(message))
        print(path.params['status'])
        await asyncio.sleep(2)  # 假装模拟去操作开关灯
        if (path.params['status'] == 'on'):
            await  websocket.send("the light has turned on")
        elif path.params["status"] == 'off':
            await  websocket.send("the light has turned off")
        else:
            await  websocket.send("invalid params")


async def main():
    # rooter是一个装饰器，它的__call__函数有三个参数，第一个参数是self。
    # 所以这里我们需要使用lambda进行一个转换操作，因为serv的wshander函数只能接收2个参数
    print("ssssss")
    async with websockets.serve(lambda x, y: router(x, y), "127.0.0.1", 8765):
        print("======")
        await  asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
