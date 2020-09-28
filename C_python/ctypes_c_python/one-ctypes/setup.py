# setup.py
from distutils.core import setup, Extension


cfile = 'sample.c'
name = str.split(cfile, '.')

# setup.py
setup(name=name[0],
      ext_modules=[
          Extension(name[0],
                    [cfile],
                    include_dirs=['/some/dir'],
                    define_macros=[('FOO', '1')],
                    undef_macros=['BAR'],
                    library_dirs=['/usr/local/lib'],
                    libraries=[name[0]]
                    )
      ]
      )
