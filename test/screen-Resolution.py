# --code=utf-8

hight = 0
width = 0
screen_size = 0
inch_mm = 0

ppi = 0






# print(d)

j = 0
L = []
s = []
d = [[5, 4], [4, 3], [16, 10], [16, 9], [21, 9]]

Resolution = [[], [], [], [], [], [], []]


screen_size = 19

def ppi(screen_size, x, y):
    ppi = (y * y + x * x)**0.5 / screen_size
    return ppi

def true_size(screen_size, x, y):
    k = screen_size / ((x * x + y * y)**0.5)
    x = round(x * k * 25.4)
    y = round(y * k * 25.4)
    return [x, y, x * y // 100]

for i in d:
    L = true_size(screen_size, i[0], i[1])
    s.append(L)
    print("尺寸:%d, 比例:%2d:%2d,   宽:%d,   高:%d, 面积(厘米):%6d" %
          (screen_size, i[0], i[1], L[0], L[1], L[2]))


print(ppi(screen_size, 1280, 1040))


print(s)
