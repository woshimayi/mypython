
# def odd(a):
# 	print 'step 1'
# 	yield 1
# 	print 'step 2'
# 	yield 3
# 	print 'step 3'
# 	yield 5

# for n in odd(4):
# 	print n


# def add(x,y,f):
# 	return f(x)+f(y)


# print add(2,-3,abs)


# def f(x,y):
# 	return x+y
# print map(f, [1,2,3,4,5,6,7,8,9])


# L = []
# for n in [1,2,3,4,5,6,7,8,9]:
# 	L.append(f(n))
# print L

# print map(str,[1,2,3,4,4,5,6,7,8,9])

# print reduce(f,[1,2,3,4,5])

# def is_odd(n):
# 	return n%2==1

# print filter(is_odd, [1,2,3,4,5,6,7,8,9,15])


# def not_emtpy(s):
# 	return s and s.strip()

# print filter(not_emtpy,['A','', 'B', None, 'C', ''])

# def reversed_cmd(x,y):
# 	if x > y:
# 		return -1
# 	if x < y:
# 		return 1
# 	return 0

# print sorted([35,23,64,34,23,35],reversed_cmd)

# def cmd_ignore_core(s1,s2):
# 	u1 = s1.upper()
# 	u2 = s2.upper()
# 	if u1 < u2:
# 		return -1
# 	if u1 > u2:
# 		return 1
# 	return 0

# print sorted(['Csd','asd','csf','fgh'],cmd_ignore_core)


# def calc_sum(*arge):
# 	ax = 0
# 	for n in arge:
# 		ax = ax + n
# 	return ax

# print calc_sum(*[1,2,3,4,5,6])

# def laxy_sum(*arg):
# 	def sum():
# 		ax = 0
# 		for n in arg:
# 			ax = ax + n
# 		return ax
# 	return sum

# f=laxy_sum(*[1,2,3,4,5,6])



def cont():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1,f2,f3 = cont()

print f1(),f2(),f3()

