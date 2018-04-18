

class Animal(object):
	def run(self):
		print 'Animal is runing!'

class Dog(Animal):
	def run(self):
		print 'Dog is runing!'

class Cat(Animal):
	def run(self):
		print 'Cat is runing!'

def run_twice(animal):
	animal.run()

class Tortoise(Animal):
	def run(self):
		print 'Tortoise is runing slowly...'


dog = Dog()
dog.run()

cat = Cat()
cat.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())

print type(dog)
print type(dog)==type(cat)
print isinstance(cat, Cat)     
print isinstance(cat, Animal)