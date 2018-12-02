import  sys
import  os


str_module = '''# coding=utf-8


if __name__ == "__main__":
	if argc > 2:
		print(argv[1])
'''

str_info = '''#########################################################################################################
     Author: baiyizhanshi
      Email: 2638288078@qq.com
create Date: 


#########################################################################################################
'''


def MyMkdir(dir):
	path=dir.strip()

	isExists = os.path.exists(dir)

	if not isExists:
		os.makedirs(dir)
		print(dir)
		# os.makedirs(dir1)
		print("create suuess")
	else:
		print("create fail")

	dir1 = '%s\%s' % (dir, 'bin')
	os.makedirs(dir1)
	file1 = '%s\%s' % (dir1, dir)
	FILE = open(file1, 'w')
	FILE.close()

	dir2 = '%s\%s' % (dir, dir)
	os.makedirs(dir2)
	dir3 = '%s\%s' % (dir2, 'tests')
	os.makedirs(dir3)
	
	file2 = '%s\%s' % (dir3, '__init__.py')
	print(file2)
	FILE = open(file2, 'w')
	FILE.write(str_module)
	FILE.close()

	file3 = '%s\%s_%s' % (dir3, dir, 'main.py')
	print(file3)
	FILE = open(file3, 'w')
	FILE.write(str_module)
	FILE.close()

	file4 = '%s\%s' % (dir2, '__init__.py')
	print(file4)
	FILE = open(file4, 'w')
	FILE.write(str_module)
	FILE.close()
	file5 = '%s\%s' % (dir2, 'main.py')
	print(file5)
	FILE = open(file5, 'w')
	FILE.write(str_module)
	FILE.close()
	
	dir4 = '%s\%s' % (dir, 'docs')
	os.makedirs(dir4)
	file6 = '%s\%s' % (dir4, 'conf.py')
	FILE = open(file6, 'w')
	FILE.write(str_module)
	FILE.close()
	file7 = '%s\%s' % (dir4, 'abc.rst')
	FILE = open(file7, 'w')
	FILE.close()

	file8 = '%s\%s' % (dir, "setup.py")
	FILE = open(file8, 'w')
	FILE.write(str_module)
	FILE.close()

	file9 = '%s\%s' % (dir, "requirements.txt")
	FILE = open(file9, 'w')
	FILE.close()

	file10 = '%s\%s' % (dir, "README")
	FILE = open(file10, 'w')
	FILE.close()



if __name__ == "__main__":
	print(sys.argv[1])
	MyMkdir(sys.argv[1])
	