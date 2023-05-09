#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: garner
@file: num_1.py
@time: 23/5/5 19:19
@desc:
'''

import numpy as np
from matplotlib import pyplot as plt
import time
from scipy.interpolate import make_interp_spline


class PID():
    def __init__(self, P, I, D):  # 父类初始化
        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.sample_time = 0.00
        self.current_time = time.time()
        self.last_time = self.current_time
        self.clear()

    def clear(self):  # 初始化
        self.SetPoint = 0.0
        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0
        self.last_error = 0.0
        self.last_last_error = 0.0
        # self.int_error = 0.0
        self.windup_guard = 20.0  ###积分限幅
        self.output = 0.0

    def update_position(self, feedback_value):  #####位置式pid  (这个程序把T用进去了***)  kp=kp  ki=kp/Ti    kd=kp*Td   delta_time是采样周期T
        error = self.SetPoint - feedback_value
        self.current_time = time.time()
        delta_time = self.current_time - self.last_time  # 采样周期T
        delta_error = error - self.last_error  # e-e1
        if (delta_time >= self.sample_time):  ##如果采样周期大于0
            self.PTerm = self.Kp * error  # 比例
            self.ITerm += error * delta_time  # 积分   # 位置式pid 求和
            if self.ITerm < -self.windup_guard:  ##积分限幅   #位置式PID在积分项达到饱和时,误差仍然会在积分作用下继续累积，一旦误差开始反向变化，系统需要一定时间从饱和区退出，所以在u(k)达到最大和最小时，要停止积分作用，并且要有积分限幅和输出限幅
                self.ITerm = -self.windup_guard
            elif self.ITerm > self.windup_guard:
                self.ITerm = self.windup_guard
            self.DTerm = 0.0
            if delta_time > 0:
                self.DTerm = delta_error / delta_time
            self.last_time = self.current_time  # 更新上次时间
            self.last_error = error  # 更新上次误差
            self.output = self.PTerm + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)

    def update_increment(self, feedback_value):  ##增量式pid###可以只做PI控制
        error = self.SetPoint - feedback_value
        self.output += self.Kp * (error - self.last_error) + self.Ki * error + self.Kd * (
                error - 2 * self.last_error + self.last_error)
        self.last_error = error
        self.last_last_error = self.last_error

        # 感觉没用 只是一些说明
    # def setKp(self, proportional_gain):
    #     self.Kp = proportional_gain
    #
    # def setKi(self, integral_gain):
    #     self.Ki = integral_gain
    #
    # def setKd(self, derivative_gain):
    #     self.Kd = derivative_gain
    #
    # def setWindup(self, windup):
    #     self.windup_guard = windup
    #
    # def setSampleTime(self, sample_time):
    #     self.sample_time = sample_time


def test_pid(P=0.2, I=0.0, D=0.0, L=100):
    """Self-test PID class

    .. note::
      ...
      for i in range(1, END):
        pid.update(feedback)
        output = pid.output
        if pid.SetPoint > 0:
          feedback += (output - (1/i))
        if i>9:
          pid.SetPoint = 1
        time.sleep(0.02)
      ---
    """
    pid = PID(P, I, D)  ##调用PID类

    pid.SetPoint = 0.0  # 前9s设定0  后面设定自己想要的值
    # pid.setSampleTime(0.01)#####################

    END = L
    feedback = 0

    feedback_list = []  ##反馈列表
    time_list = []  ##时间  列表
    setpoint_list = []  ##设定列表

    for i in range(1, END):
        pid.update_increment(feedback)  ###选择pid类型 增量pid
        output = pid.output
        if pid.SetPoint > 0:  # 到了第9s
            feedback += output  # (output - (1/i))控制系统的函数   #
        if i > 9:
            pid.SetPoint = 10  ##前9s 输出0###########################################################################380
        # time.sleep(0.01) ## 延时0.01s ##使点 少一些 #使仿真更直观

        feedback_list.append(feedback)
        setpoint_list.append(pid.SetPoint)  # [0,0,0,0,0,0,0,0,0,1,1,1,...]
        time_list.append(i)  ##[1,2,...,L]
        # print(feedback_list)
    time_sm = np.array(time_list)  ##x [1 2 3 ... L]
    feedback_sm = np.array(feedback_list)  ##y

    time_smooth = np.linspace(time_sm.min(), time_sm.max(), 300)  ###x_smooth 等差

    feedback_smooth = make_interp_spline(time_sm, feedback_sm)(time_smooth)  #####y_smooth 线性插值

    plt.figure("PID仿真")  # 窗口名
    plt.plot(time_smooth, feedback_smooth)  ####反馈的pid线
    plt.plot(time_list, setpoint_list)  ##设定的pid

    plt.xlim((0, L))  ### L 时间长度##横坐标的范围 (0,l)
    plt.ylim((min(feedback_list) - pid.SetPoint * 0.5, max(feedback_list) + pid.SetPoint * 0.5))  ##设置纵坐标范围

    plt.xlabel('time (s)')
    plt.ylabel('PID (PV)')
    plt.title('TEST PID')

    # plt.ylim((1 - 0.5, 1 + 0.5)) ##设置纵坐标范围(0.5,1.5)

    plt.grid(True)  ##有 坐标方格
    plt.show()


if __name__ == "__main__":
    test_pid(0.85, 0.001, 0.000, L=30)
    # test_pid(0.68,0.010,0.05, L=100)
    print('hello world')
