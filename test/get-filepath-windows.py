# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:18:43 2019

author: Irvinfaith
email: Irvinfaith@hotmail.com
"""
import sys
import subprocess


class get_pwd():
    """
    Main class to pass a path of target file to console.
    """
    def __init__(self, path):
        self.path = path
        
    def pwd_1(self):
        """
        Return path splits with double backslash.
        """
        path_1 = self.path.replace('\\', '\\\\')
        return self.copy_to_clipboard(path_1)
    
    def pwd_2(self):
        """
        Return path splits with slash.
        """
        path_2 = self.path.replace('\\', '/')
        return self.copy_to_clipboard(path_2)
    
    def copy_to_clipboard(self, txt):
        """
        Copy path and add double quote into clipboard.
        
        """
        cmd = 'echo "' + txt.strip() + '"|clip'
        return subprocess.check_call(cmd, shell=True)


if __name__ == '__main__':
    gp = get_pwd(sys.argv[2])
    if sys.argv[1] == 'path_1':
        gp.pwd_1()
    elif sys.argv[1] == 'path_2':
        gp.pwd_2()
    else:
        pass