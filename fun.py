def my_abs(x):
	if not isinstance (x,(int,float)):
		raise TypeError('bad operand Type')
	if x >= 0:
		return x
	else:
		return -x

print my_abs(23.4)


def  fun(x,y,k):
	return x,y,k

print fun(3,4,6)

def enroll(name,gender,age=6,city='beijing'):
	print 'name:', name
	print 'gender:',gender
	print 'age' , age
	print 'city', city

print enroll('bob','F')

print enroll('bob','M',7)


def add_end(L=None):
	L.append('END')
	return L

print add_end([3,5.6,6,'wer'])

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

num=[1,2,3]
print calc(num[0],num[1],num[2])