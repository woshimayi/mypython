#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: deamoncao100@gmail.com
@software: garner
@file: client_dof.py
@time: 22/10/30 15:24
@desc:
'''

import asyncio
import websockets

async def hello():
    try:
        async with websockets.connect('ws://127.0.0.1:8765/light/on') as websocket:
            light_addr = 'Hello world'
            await websocket.send(light_addr)
            recv_msg = await websocket.recv()
            print(recv_msg)

    except websockets.exceptions.ConnectionClosedError as e:
        print("connection closed error")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    renwu = [hello()]
    loops = asyncio.get_event_loop()
    loops.run_until_complete(asyncio.wait(renwu))
