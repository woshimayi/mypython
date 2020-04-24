# --code=utf-8

Resolution = 0
hight = 0
width = 0
screen_size = 0
inch_mm = 0;

ppi = 0


def ppi(x, y):
	ppi = (hight*hight + width*width)**0.5/screen_size


def true_size(screen_size, x, y):
	k = screen_size/((x*x + y*y)**0.5)
	x = round(x*k*25.4)
	y = round(y*k*25.4)

	return [x, y, x*y//100]


d = [[5,4], [4,3], [16,10], [16,9], [21,9]]
# print(d)

j = 0
L = []
s = []
screen_size = 27
for i in d:
	# print(i[0], i[1], end='')
	L = true_size(screen_size, i[0], i[1])
	s.append(L)
	# print('尺寸:'screen_size, '  比例:'i, '  宽:'L[0], '  高:'L[1], '  面积(/厘米)'L[2])
	print("尺寸:%d, 比例:%2d:%2d,   宽:%d,   高:%d, 面积(/厘米):%6d" % (screen_size, i[0], i[1], L[0], L[1], L[2]))

print(s)
