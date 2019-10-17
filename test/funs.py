
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

num = [1,2,3]
print calc(*num)


def person(name, age, **key):
	print 'name:',name , 'age:',age, 'other:', key


num = {'1':'sd','3':'wer'}
print person('bob', 8, **num)

print person('bob', 8, other={'city':'beijing'})

def func(a,b,*age,**key):
	print 'a=',a, 'b=',b, 'age=', age, 'key=', key

print func(1,4,*(1,2,3), other={'asd':'sss'})


def fact(n):
	if n==1:
		return n
	return n*fact(n-1)

print fact(1000)