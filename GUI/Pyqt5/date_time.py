#!/usr/bin/python3

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()


print(now.toString())
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate) + '\n')

# 确定当前日期
datetime = QDateTime.currentDateTime()  

print(datetime.toString())
print(datetime.toString(Qt.ISODate))
print(datetime.toUTC().toString(Qt.ISODate))
print(datetime.toString(Qt.DefaultLocaleLongDate) + '\n')


# 当前时间
time = QTime.currentTime()

# print(Qt.DefaultLocaleLongDate)
print(time.toString())
print(time.toString(Qt.DefaultLocaleLongDate))


now = QDateTime.currentDateTime()

print("local datetime:", now.toString(Qt.ISODate))
print("Universal datetime: ", now.toUTC().toString(Qt.ISODate))
print("The offset from UTC is {0} secend".format(now.offsetFromUtc()) + '\n')



d = QDate.currentDate()
print("Days in month: {0}".format(d.daysInMonth()))
print("Days in year: {0}".format(d.daysInYear()) + '\n')



mxas1 = QDate(2017, 12, 24)
mxas2 = QDate(2018, 12, 24)

now = QDate.currentDate()

dayspassed = mxas1.daysTo(now)
print("{0} days have passed since last Xmas".format(dayspassed))

nofdays = now.daysTo(mxas2)
print("There are {0} days until next XMas".format(nofdays))