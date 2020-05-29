import os
import sys
import datetime
import time
import math


UTo = 180

days_of_month_1=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days_of_month_2=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# // 判断是否为闰年：若为闰年，返回1；若不是闰年, 返回0

def leap_year(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return 1
    else:
        return 0

print(leap_year(2001))


def days(year, month, date):
    a = 0
    for i in range(2000, year):
        if leap_year(i):
            a = a + 366
        else:
            a = a + 365

    i = 0
    if leap_year(year):
        for i in range(12):
            a = a + days_of_month_2[i]
    else:
        for i in range(12):
            a = a + days_of_month_1[i]

    a = a + date
    return a

print(days(2020, 5, 3))


# 求格林威治时间公元2000年1月1日到计算日的世纪数

t_century = (days(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday) + UTo/360) / 36525;

print(t_century)

L_sun = 280.460 + 36000.770 * t_century
print("L_sun", L_sun)

G_sun = 357.528 + 35999.050 * t_century
print("G_sun", G_sun)

ecliptic_longitude =  L_sun + 1.915 * math.sin(G_sun * math.pi / 180) + 0.02 * math.sin(2 * G_sun * math.pi / 180)
print("ecliptic_longitude", ecliptic_longitude)

earth_tilt = 23.4393 - 0.0130 * t_century
print("earth_tilt", earth_tilt)

#  求太阳偏差
sun_deviation =  180 / math.pi * math.asin(math.sin(math.pi / 180 * earth_tilt) * math.sin(math.pi / 180 * ecliptic_longitude))

GHA = GHA = UTo - 180 - 1.915 * math.sin(G_sun * math.pi / 180) - 0.02 * math.sin(
    2 * G_sun * math.pi / 180) + 2.466 * math.sin(2 * ecliptic_longitude * math.pi / 180) - 0.053 * math.sin(
    4 * ecliptic_longitude * math.pi / 180)
print("GHA", GHA)

#  求修正值e
h = 10
glat = 31.1
e= 180 / math.pi * math.acos(
    (math.sin(h * math.pi / 180) - math.sin(glat * math.pi / 180) * math.sin(sun_deviation * math.pi / 180)) / (
                math.cos(glat * math.pi / 180) * math.cos(sun_deviation * math.pi / 180)))
print("e", e)

# 求时区

def Zone(glong):
    if glong>=0:
        return (glong/15.0)+1
    else:
        return (glong/15.0)-1


glong = Zone(121.1)
# // 求日出时间
sunrise = UTo - (GHA + glong + e)
print("sunrise", sunrise)


# // 求日落时间
sunset =  UTo - (GHA + glong - e)
print("sunset", sunset)

print((sunset/15+8)+":"+(60*(sunset/15+8-(sunset/15+8))))