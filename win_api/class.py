
# 访问限制  和 私有变量


import os

class Student(object):
	def __init__(self,name, score):
		self.__name = name
		self.__score = score

	def get_grand(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 80:
			return 'B'
		else:
			return 'C'

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_name(self,name):
		self.__name = name

	def set_score(self, score):
		self.__score = score



s = Student('bob', 96)

print s.get_grand()
print s.get_name(), s.get_score()

s.set_name('jack')
s.set_score(100)

print s.get_grand()
print s.get_name(), s.get_score()