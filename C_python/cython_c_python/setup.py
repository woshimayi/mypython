# -*- coding: UTF-8 -*- 
 
from distutils.core import setup, Extension

cfile = 'Extest.c'
name = str.split(cfile, '.')

setup(name=name[0], ext_modules=[Extension(name[0], sources=[cfile])])