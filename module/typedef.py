# try:
# 	import cStringIO as cStringIO
# except ImportError:
# 	import StringIO


def _provate_l(name):
	return 'Hello ,%s' % name

def _private_2(name):
	return 'Hi, %s' % name

def greeting(name):
	if len(name) > 3:
		return _provate_l(name)
	else:
		return _private_2(name)

print greeting("asdasdasdas")