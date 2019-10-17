
import os

# f = open('./super.py','r')
# x=0
# # for x in  

# print f.read()
# f.close()





def getDocSize(path):
	try:
		size = os.path.getsize(path)
		return size
	except :
		print 'err'

def getFileInfo(inputfile = None, fileInfo = None):
	L=[]
	L= 'path='
	L += os.path.abspath('.')
	L += 'fileSize='
	L += '%s' % getDocSize('./123.py')

	print L,'byte'

	return L == type('qwer')

print  getFileInfo("./123.py")



# print [x for x in os.listdir('.') if os.path.isdir(x)]
# print ""

# print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]]


