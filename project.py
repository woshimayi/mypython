
def now():
	print '2015'

# f = now

# print f()

print f.__name__

def func(*arges,*kw):
	retrun 

def log(func):
	def wrapper(*arges,**kw):
		print 'call %s():' % func.__name__
		return func(*arges,*kw)
	return wrapper

print now()

