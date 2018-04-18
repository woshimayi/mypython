# -*- coding: utf-8 -*-

import win32gui
import re
import SendKeys
import time

class WindowFinder:
    """Class to find and make focus on a particular Native OS dialog/Window """

    def __init__ (self):
        self._handle = None

    def find_window(self, class_name, window_name = None):
        """Pass a window class name & window name directly if known to get the window """
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        '''Call back func which checks each open window and matches the name of window using reg ex'''
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) != None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """ This function takes a string as input and calls EnumWindows to enumerate through all open windows """

        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """Get the focus on the desired open window"""
        win32gui.SetForegroundWindow(self._handle)

def send_keys_to_dialog(title=r".*Upload.*", key_valus=r""):
    win_dialog = WindowFinder()

    win_dialog.find_window_wildcard(title) 
    win_dialog.set_foreground()

    time.sleep(2)

    SendKeys.SendKeys(key_valus)
    SendKeys.SendKeys("{ENTER}")

if __name__ == "__main__":
    send_keys_to_dialog(u"Open", r"E:\documents\Selenium.docx")