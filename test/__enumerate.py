fruits = ['orange', 'grape', 'pitaya', 'blueberry']
for index, fruit in enumerate(fruits):
	print(index, ':', fruit)


keys = ['1001', '1002', '1003']
values = ['骆昊', '王大锤', '白元芳']
d = dict(zip(keys, values))
print(d)