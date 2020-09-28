# coding=utf-8
#
"""
mydir.py: a module that lists the names of other module
"""
seplen = 60
sepchr = '-'


def listing(module, verbose=True):
    seplen = sepchr * seplen
    if verbose:
        print(seplen)
        print('name', module.__name_ -, 'file:', module.__file)
        print(seplen)
    count = 0
    for attr in module.__dict__:
        print('%02d %s') % (count, attr), end = ''
        if attr.startswith('__'):
            print('<built-in name>')
        else:
            print(getattr(module, attr))
        count += 1

    if verbose:
        print(seplen)
        print(module.__name__, 'has %d names' % count)
        print(seplen)


if __name__ == '__mian__':
    import mydir
    listing(mydir)
