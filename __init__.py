
类和实例
class Student(object):
	def __init__(self, name, score):
		self.name = name 
		self.score = score

bart = Student('bob',45)
# bart.name = 'Bart simpson'
# 类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数和关键字参数。
#  默认参数 num 可变参数  *num 关键字参数 **num


# print bart.name, bart.score

# 数据封装

class Tench(object):
	def __init__(self, name, arg):
		self.name = name
		self.arg = arg


	def print_score(self):
		print '%s,%s' % (self.name, self.score)

bart = Tench('jack', 45)

print bart.print_score()
