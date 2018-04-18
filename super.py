

class Animal(object):
	def run(self):
		print 'Animal is runing '

class Cat(Animal):
	def run(self):
		print 'cat is runing '

class Dog(Animal):
	def run(self):
		print 'dog is runing '

def  run_sdf(animal):
	animal.run()
	



# dog = Dog()
# cat = Cat()

# print dog.run()
# print cat.run()

# print isinstance(dog,Animal)
# print isinstance(cat,Animal)
# print isinstance(cat,Cat)

run_sdf(Dog())
run_sdf(Cat())

