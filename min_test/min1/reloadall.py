
#coding = utf-8

"""
reloadall.py: transitively relaod nested modules
"""

import types
form imp import reload


def status(module):
    print 'reloading' + module.__name__


def transitive_reload(module, visites):
    if module not in visites:
        status(module)
        reload(module)
        visites[module] = None
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                transitive_reload(attrobj, visited)


def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)


if __name__ == '__main__':
    import reloadall
    reload_all(reloadall)
