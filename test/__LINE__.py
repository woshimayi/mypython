import sys

def __LINE__():
    print '['+sys._getframe().f_code.co_filename+']'+'['+sys._getframe(1).f_code.co_name+']'+'[',sys._getframe().f_back.f_lineno,']'




def fun():
    __LINE__()
    

fun()

