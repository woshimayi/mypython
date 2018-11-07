

class Student(object):
	__slots__ = ('name', 'age', 'score') # 用tuple 绑定允许绑定的属性

# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

# 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：

s = Student()
s.name = 'bob'
s.age = 25
s.score = 99

print s.name, s.age, s.score
		