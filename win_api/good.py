
import os

# for i, value in enumerate(['A','B','C']):
# 	print i, value


# for x, y in [(1,1),(2,4),(3,9)]:
# 	print x,y


# for d in os.listdir('./'):
# 	print d,'1'

# d = {'x':9,'v':'5','g':7}
# for k, v in d.iteritems():
# 	print k, '=', v


# A = {'a':'b','c':'d','e':'f'}
# for k, v in A.iteritems():
# 	print k, '=' , v


# g = (x*x for x in range(10))

# for n in g:
# 	print n


def fib(max):
	n, a, b =0,0,1
	while n < max:
		yield b
		a,b = b, a+b
		n=n+1

print fib(5)

