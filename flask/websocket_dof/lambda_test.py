x = lambda a: a + 10
print(x(3))

x = lambda a, b: a + b
print(x(3, 5))


def add_dof(x, y, z):
    print(x, y, z)
    return x + y + z


x = lambda x, y, z: add_dof(x, y, z)
print(x('asd', '80', 'sss'))

L = [x * x for x in range(10)]
print(L)


def test():
    i = 0
    for i in range(10):
        temp = yield i
        print(temp)


# L = test()

# print(L.__next__())
# print(L.__next__())
# print(L.__next__())
# print(L.send('xxxx'))

# print(L)

# g = (x * x for x in range(10))
# print(g)
#


def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    return greet
    # print(greet())
    # print(welcome())
    # print("now you are back in the hi() function")


# a = hi()
# print(a)
# print(a())
# print(hi()())
# greet()

def a_new_decorator(a_fun):

    def welcome():
        print("4 xxxxxx")
        return "now you are in the welcome() function"

    def wrapTheFunction():
        print("1 xxxxxx")

        a_fun()

        print('2 xxxxxx')


    # return wrapTheFunction
    return welcome

def a_function_requiring_decoration():
    print('3 xxxxx')

'''
# a_function_requiring_decoration()

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)


a_function_requiring_decoration()
'''

@a_new_decorator
def a_function_requiring_decoration():
    print("1 zzz")

a_function_requiring_decoration()

print(a_function_requiring_decoration.__name__)

