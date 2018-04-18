
std1 = {'name': 'bob','score': '34'}
std2 = {'name': 'jack', 'score': '45'}

# def print_score(std):
# 	print '%s: %s' % (std['name'],std['score'])

# print print_score(std1)


class Student(object):

	def __init__(self,name,score):
		self.name = name
		self.score = score

	def porint_score():
		print '%s: %s' % (self.name , self.score)


bart = Student('bob',45)
lisa = Student('Lisa Simpson',87)

print bart.print_score()
print Lisa.print_score()