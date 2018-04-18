import sys

def PP(*a):
    print '['+sys._getframe().f_code.co_filename+']'+'['+sys._getframe(1).f_code.co_name+']'+'['+':',sys._getframe().f_back.f_lineno,']',
    for e in a:
    	# print namestr(e, locals())
    	print  '['+e.__class__.__name__, e,']',
    print 

def main():
	a = 2
	b = 5
	c = 's'
	d = 'sdfsdf'
	PP(a,b,c,d)
	PP()



if __name__ == '__main__':
	main()