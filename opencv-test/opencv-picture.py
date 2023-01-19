#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: opencv-picture.py
@time: 2020/8/14 11:39
@desc:
'''
import cv2
import numpy as np

"""
:param
    无
:return
    无
功能：调用笔记本摄像头获取视频图片
"""


# 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
cap = cv2.VideoCapture(0)
while True:
    # 从摄像头读取图片
    sucess, img = cap.read()
    # 转为灰度图片
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    # 显示摄像头，背景是灰度。
    cv2.imshow("img", gray)
    # 保持画面的持续。
    k = cv2.waitKey(1)
    if k == 27:
        # 通过esc键退出摄像
        cv2.destroyAllWindows()
        break
    elif k == ord("s"):
        # 通过s键保存图片，并退出。
        cv2.imwrite("image2.jpg", img)
        cv2.destroyAllWindows()
        break
# 关闭摄像头
cap.release()


'''
# Load an color image in grayscale
img = cv2.imread('123.jpg',0)
print(img)

# 显示图像
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 一 种 特 殊 的 情 况 是， 你 也 可 以 先 创 建 一 个 窗 口， 之 后再 加 载 图 像 可以修改窗口大小
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存图像
cv2.imwrite('messigray.png',img)
'''

'''
# 下面的程序将会加载一个灰度图，显示图片，按下’s’键保存后退出，或者按下 ESC 键退出不保存
img = cv2.imread('123.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
'''


'''
from matplotlib import pyplot as plt

img = cv2.imread('123.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

'''


'''
# 用摄像头捕获视频
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

'''


'''
# 从文件中播放视频
import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''

'''
# 保存视频

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

'''

'''
# 画图形
# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px 画一条蓝线
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# 话矩形
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
# 画圆
cv2.circle(img,(447,63), 63, (0,0,255), -1)
# 椭圆
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# 画多边形
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

# 在图片上添加文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

# 显示图像
cv2.imshow('image', img)
# 等待按键后，退出
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
# 双击画圆
# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


# Create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        continue
        # break
cv2.destroyAllWindows()


'''

'''
# 拖动鼠标时绘制矩形或者是圆圈
drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1

# mouse callback function


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                # cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
                pass
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)


# Next we have to bind this mouse callback function to OpenCV # # window.
# In the main loop, we should set a keyboard binding for # key ‘m’ to
# toggle between rectangle and circle.
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):  # 切换模式
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()

'''


'''
# 用滑动条做调色板
import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
'''


# '''
# 综合以上练习 综合为一下程序


'''
def nothing(x):
    pass


# 当鼠标按下时变为 True
drawing = False
# 如果 mode 为 true 绘制矩形。按下 'm' 变成绘制曲线。
mode = True
ix, iy = -1, -1
# 创建回调函数


def draw_circle(event, x, y, flags, param):
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    color = (b, g, r)
    global ix, iy, drawing, mode
    # 当按下左键是返回起始位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    # 当鼠标左键按下并移动是绘制图形。 event 可以查看移动， flag 查看是否按下
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing:
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), color, -1)
            else:
                # 绘制圆圈，小圆点连在一起就成了线， 3 代表了笔画的粗细
                cv2.circle(img, (x, y), 3, color, -1)
                # 下面注释掉的代码是起始点为圆心，起点到终点为半径的
                # r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                # cv2.circle(img,(x,y),r,(0,0,255),-1)
                # 当鼠标松开停止绘画。
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False


        # if mode==True:
        # cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        # else:
        # cv2.circle(img,(x,y),5,(0,0,255),-1)
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.setMouseCallback('image', draw_circle)
while(1):
    cv2.imshow('image', img)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
'''
