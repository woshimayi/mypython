# -*- coding: utf-8 -*-
import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class IndexScreen(GridLayout):
    def __init__(self, **kwargs):
        super(IndexScreen, self).__init__(**kwargs)
        pass

# 这里不能直接使用App作为你自己创建的应用类的类名
class TestApp(App):
    def build(self):
        return IndexScreen()

if __name__ == '__main__':
    TestApp().run()