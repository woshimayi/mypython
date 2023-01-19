#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: usb-test.py
@time: 2020/9/3 15:58
@desc:
'''


import usb.util
import usb.core


dev = usb.core.find()
print('0x%x' % dev.bLength)
print('0x%x' % dev.idVendor)
print('0x%x' % dev.idProduct)
print('0x%x' % dev.bcdDevice)


class find_class(object):
    def __init__(self, class_):
        self._class = class_

    def __call__(self, device):
        # first, let's check the device
        if device.bDeviceClass == self._class:
            return True
        # ok, transverse all devices to find an
        # interface that matches our class
        for cfg in device:
            # find_descriptor: what's it?
            intf = usb.util.find_descriptor(
                cfg,
                bInterfaceClass=self._class
            )
            if intf is not None:
                return True

        return False


# dev = usb.core.find(find_all=1, custom_match=find_class(7))

for cfg in dev:
    print(str(cfg.bConfigurationValue))
    # print('Decimal VendorID=0x%x ProductID = 0x%x' % (cfg.idVendor, cfg.idProduct))
    for intf in cfg:
        print('bInterfaceNumber = 0x%x, intf.bAlternateSetting = 0x%x' %
              (intf.bInterfaceNumber, intf.bAlternateSetting))
        for ep in intf:
            print('bEndpointAddress = 0x%x' % ep.bEndpointAddress)
            print('')


dev.set_configuration()


def rx_loop():
    while (True):
        try:
            # read(endpoint, size_or_buffer, timeout = None)
            data = dev.read(0x1, 1, 1000)
            print(data)
        except Exception as e:
            print(e)


def tx_loop():
    while (True):
        try:
            # write(endpoint, data, timeout = None)
            data = dev.write(0x81, 1, 1000)
            print(data)
        except Exception as e:
            print(e)

# rx_loop()

alt = usb.util.find_descriptor(cfg, find_all=True, bInterfaceNumber=1)

print(alt)