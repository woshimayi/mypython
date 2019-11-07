import os
import sys
import struct
import array
from fcntl import ioctl



class self.XBOX():
    def __init__(self):

        self.axis_states = {
            'LX': 0,
            'LY': 0,
            'RX': 0,
            'RY': 0,
            'LT': 0,
            'RT': 0,
            'XX': 0,
            'YY': 0,
        }
        self.button_states = {
            'A': 0,
            'B': 0,
            'X': 0,
            'Y': 0,
            'LB': 0,
            'RB': 0,
            'START': 0,
            'BACK': 0,
            'HOME': 0,
            'LO': 0,
            'RO': 0,
        }

        # 先前校验时，方向盘是x,左侧踏板是z,右侧踏板是rz。

        self.self.XBOX_TYPE_BUTTON = 0x01
        self.self.XBOX_TYPE_AXIS = 0x02

        self.self.XBOX_BUTTON_A = 0x00
        self.self.XBOX_BUTTON_B = 0x01
        self.self.XBOX_BUTTON_X = 0x02
        self.self.XBOX_BUTTON_Y = 0x03
        self.self.XBOX_BUTTON_LB = 0x04
        self.self.XBOX_BUTTON_RB = 0x05
        self.self.XBOX_BUTTON_START = 0x06
        self.self.XBOX_BUTTON_BACK = 0x07
        self.self.XBOX_BUTTON_HOME = 0x08
        self.self.XBOX_BUTTON_LO = 0x09  # /* 左摇杆按键 */
        self.self.XBOX_BUTTON_RO = 0x0a  # /* 右摇杆按键 */

        self.self.XBOX_BUTTON_ON = 0x01
        self.self.XBOX_BUTTON_OFF = 0x00

        self.self.XBOX_AXIS_LX = 0x00  # /* 左摇杆X轴 */
        self.self.XBOX_AXIS_LY = 0x01  # /* 左摇杆Y轴 */
        self.self.XBOX_AXIS_RX = 0x03  # /* 右摇杆X轴 */
        self.self.XBOX_AXIS_RY = 0x04  # /* 右摇杆Y轴 */
        self.self.XBOX_AXIS_LT = 0x02
        self.self.XBOX_AXIS_RT = 0x05
        self.self.XBOX_AXIS_XX = 0x06  # /* 方向键X轴 */
        self.self.XBOX_AXIS_YY = 0x07  # /* 方向键Y轴 */

        self.self.XBOX_AXIS_VAL_UP = -32767
        self.self.XBOX_AXIS_VAL_DOWN = 32767
        self.self.XBOX_AXIS_VAL_LEFT = -32767
        self.self.XBOX_AXIS_VAL_RIGHT = 32767

        self.self.XBOX_AXIS_VAL_MIN = -32767
        self.self.XBOX_AXIS_VAL_MAX = 32767
        self.self.XBOX_AXIS_VAL_MID = 0x00

        self.axis_map = []
        self.axis_names = {
            0x00: 'x',
            0x02: 'z',
            0x05: 'rz',
        }

        fn = '/dev/input/js0'
        jsdev = open(fn, 'rb')
        # # Get the device name.
        buf = array.array('u', ['\0'] * 5)
        ioctl(jsdev, 0x80006a13 + (0x10000 * len(buf)), buf)  # JSIOCGNAME(len)
        js_name = buf.tostring()
        print('Device name: %s' % js_name)

        # Get number of axes and buttons.
        buf = array.array('B', [0])
        ioctl(jsdev, 0x80016a11, buf)  # JSIOCGAXES
        num_axes = buf[0]

        # Get the axis map.
        buf = array.array('B', [0] * 0x40)
        ioctl(jsdev, 0x80406a32, buf)  # JSIOCGAXMAP
        num_buttons = buf[0]
        print(num_buttons, num_axes)

    def xobx_read():
        # Main event loop
        while True:
            evbuf = jsdev.read(8)
            if evbuf:
                time, value, type, number = struct.unpack('IhBB', evbuf)   # 将linux C 字节流转换为Python数据类型
                if type & 0x01:
                    if number == self.XBOX_BUTTON_A:
                        button_states["A"] = value
                    elif number == self.XBOX_BUTTON_B:
                        button_states["B"] = value
                    elif number == self.XBOX_BUTTON_X:
                        button_states["X"] = value
                    elif number == self.XBOX_BUTTON_Y:
                        button_states["Y"] = value
                    elif number == self.XBOX_BUTTON_LB:
                        button_states["LB"] = value
                    elif number == self.XBOX_BUTTON_RB:
                        button_states["RB"] = value
                    elif number == self.XBOX_BUTTON_START:
                        button_states["START"] = value
                    elif number == self.XBOX_BUTTON_BACK:
                        button_states["BACK"] = value
                    elif number == self.XBOX_BUTTON_HOME:
                        button_states["HOME"] = value
                    elif number == self.XBOX_BUTTON_LO:
                        button_states["LO"] = value
                    elif number == self.XBOX_BUTTON_RO:
                        button_states["RO"] = value
                    print(button_states)
                    return button_states
                elif type & 0x02:
                    if number == self.XBOX_AXIS_LX:
                        axis_states["LX"] = value
                    elif number == self.XBOX_AXIS_LY:
                        axis_states["LY"] = value
                    elif number == self.XBOX_AXIS_RX:
                        axis_states["RX"] = value
                    elif number == self.XBOX_AXIS_RY:
                        axis_states["RY"] = value
                    elif number == self.XBOX_AXIS_LT:
                        axis_states["LT"] = value
                    elif number == self.XBOX_AXIS_RT:
                        axis_states["RT"] = value
                    elif number == self.XBOX_AXIS_XX:
                        axis_states["XX"] = value
                    elif number == self.XBOX_AXIS_YY:
                        axis_states["YY"] = value
                    print(axis_states)
                    return axis_states
                    
                    


x = 