'a test module'

__author__ = 'zhengsen'

import sys


def test():
    arges = sys.argv
    if len(arges) == 1:
        print 'Hello World!'
    elif len(arges) == 2:
        print 'Hello , %s!' % arges[1]
    else:
        print 'Too many argements!'


if __name__ == '__main__':
    test()
