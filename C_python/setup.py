# -*- coding: UTF-8 -*- 
 
from distutils.core import setup, Extension
 
MOD = 'Extest'
setup(name=MOD, ext_modules=[Extension(MOD, sources=['Extest2.c'])])