import numpy as np 
# my_array = np.array([1, 2, 3, 4, 5])
# print(my_array)
#
# print(my_array[0])
# print(my_array[1])
# my_array[1] = 4
# print(my_array[1])
# print(my_array)
#
# my_new_array =  np.zeros((5))
# print(my_new_array)
#
# my_new_array =  np.random.random(5)
# print(my_new_array)
#
# my_new_array =  np.zeros((2,3))
# print(my_new_array)
#
# my_new_array =  np.ones((2,4))
# print(my_new_array)
#
# my_new_array =  np.array([[2,3], [4,5]])
# print(my_new_array)
# print(my_new_array.shape)

# a =  np.array([[2.0,3.0], [4.0,5.0]])
# b =  np.array([[6.0,7.0], [8.0,9.0]])
#
# print(a)
# print(b)
#
# print(a+b)
# print(a*b)
# print(a/b)
#
# print('aaa', a.dot(b))   # 矩阵计算

# 1D Array
# a = np.array([0, 1, 2, 3, 4])
# b = np.array((0, 1, 2, 3, 4))
# c = np.arange(5)
# d = np.linspace(0, 2*np.pi, 5)
#
# print(a)
# print(b)
# print(c)
# print(d)
# print(a[3])
#
# print('pi', np.pi)
#
#
# a = np.array([[11, 12, 13, 14, 15],
#             [16, 17, 18, 19, 20],
#             [21, 22, 23, 24, 25],
#             [26, 27, 28, 29, 30],
#             [31, 32, 33, 34, 35]])
#
#
#
#
# print(a.shape)
#
# print(a[2,4])
#
#
#
# print(a[0, 0:4])
# print(a[0:4, 0])
# print(a[::2, ::2])
#
#
# print('1', a[2:])
# print('1', a[2::])
#
# print('2', a[:, 1])
# print('3', a[1, :])
#
# print(a[:, 1].dot(a[1, :]))
#
# print(type(a)) # >>><class 'numpy.ndarray'>
# print(a.dtype) # >>>int64
# print(a.size) # >>>25
# print(a.shape) # >>>(5, 5)
# print(a.itemsize) # >>>8
# print(a.ndim) # >>>2
# print(a.nbytes) # >>>200



# a = np.arange(25)
# a = a.reshape((5, 5))  # 组成 5 *  5 的矩阵
#
# b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
#               4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
#               56, 3, 56, 44, 78])
# b = b.reshape((5,5)) # 组成 5 *  5 的矩阵
#
# print('a', a)
# print('b', b)


# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a ** 2)
# print(a < b)

# print(a > b)

# print(a.dot(b))
#
# print(a.sum())
# print(a.max())
# print(a.min())
# print(a.cumsum())
# print(a.cumsum().reshape(5, 5))

# a = np.arange(0, 100, 10)
# print('a', a)
#
# indices = [1, 5, -2]
# print(a[indices])

import matplotlib.pyplot as plt

# a = np.linspace(0, 4*np.pi, 100)
# b = np.sin(a)
# b = np.cos(a)
#
# print(a)
# print(b)
#
# plt.plot(a, b)
# mask = b >= 0
# print('mask', mask)

# plt.plot(a, b, 'go')
# plt.plot(a[mask], b[mask], 'bo')
# mask = (b >= 0) & (a <= np.pi/2)
# plt.plot(a[mask], b[mask], 'go')
# plt.plot(a[mask], b[mask], 'go')
# plt.show()


# a = np.arange(0, 100, 10)
# print('a', a)
# b = np.where(a < 50)
# print('b', b)
#
# c = np.where(a >= 50)[0]
# print('c', c)

# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
#
# b = a[:2, 1:3]
#
# print(a)
# print(b)
#
# print(a[0,1])
# b[0, 0] = 77
# print(b)
# print(a[0,1])

# a = np.array([[1,2], [3,4], [5,6]])
# print(a)
#
# # print(a[[1,1]])
# # print(a[[0,0], [0,0]])
# print(a[[1,1,2]])
# print(a[[1,1,2], [0,0,1]])




# a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]], dtype=float)
#
# print(a)
#
# b = np.array([[0,2,0,1]])
# print(b)
#
# print(a[np.arange(4), b])
# # a[np.arange(4), b] += 10
#
#
#
# print(a)
#
#
# bool = (a>2)
#
# print(bool)
# print(a[bool])
# print(a[a>3])
#
# print(a.dtype)



# x = np.array([[1,2],[3,4]], dtype=np.float64)
# y = np.array([[5,6],[7,8]], dtype=np.float64)
#
# print(x)
# print(y)
#
# # print(x+y)
# #
# # print(np.add(x, y))
#
#
# print(x.dot(y))
# print(np.dot(x,y))
#
# print(np.sum(x))
# print(np.sum(x, axis=1))



# x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# v = np.array([1, 0, 1])
# vv = np.tile(v, (4, 1))



# y = np.empty_like(x)

# print('x', x)
# print('v', v)
# print('vv', vv)
# print('y', x + v)
#
# print(x[0, :] + v)
# print(y[0, :])
#
#
# for i in range(4):
#     y[i, :] = x[i, :] + v


v = np.array([1,2,3])
w = np.array([4,5])

# print('1', np.reshape(v, (3,1)))
# print('2', np.reshape(v, (3,1)) * w)
# print('3', w * np.reshape(v, (3,1)))
#
# print('4', w + np.reshape(v, (3,1)))
# print('5', np.reshape(v, (3,1)) + w)

# x = np.array([[1,2,3], [4,5,6]])
# print('6', x)
# print('7', x.T)
#
# print('8', x.T + w)
# print('9', (x.T + w).T)
#
# print('10', x + np.reshape(w, (2,1)))
#
# print(x * 2)



# a = np.arange(20)
#
# print('a', a)
# # print('a', np.reshape(a, (2,1)))
# print(np.tile(a, (4,1)))

# a = np.arange(27).reshape(3,3,3)
# print(a)

a = np.array([[1,-1,2],[3,2,0]])
print(a)

v = np.array([[2,1,3]])
# print('v', v)
v1 = np.transpose(v)
print('v1', v1)

y = np.dot(a, v1)
print('y', y)

A = np.array([[2,1,-1],[3,0,1],[1,1,-1]])
b = np.transpose(np.array([[-3,5,-2]]))


y = np.linalg.solve(A, b)
print('y-', y)



