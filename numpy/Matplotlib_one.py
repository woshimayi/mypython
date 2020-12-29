#code=utf-8

import matplotlib.pyplot as plt

'''
#创建画板1
fig = plt.figure(1) #如果不传入参数默认画板1

#第2步创建画纸，并选择画纸1
ax1=plt.subplot(2,1,1)
#在画纸1上绘图
plt.plot([1, 2, 3])

#选择画纸2
ax2=plt.subplot(2,1,2)
#在画纸2上绘图
plt.plot([4, 5, 6])

#显示图像
plt.show()
'''

x = [1,2,3,4]
y = [4,5,6,15]

plt.plot(x,y, color='r', marker='o', linestyle='dashed')
plt.xlabel("x")
plt.ylabel('y')
plt.title(r'折线')
plt.axis([0,6,0,20])
plt.show()