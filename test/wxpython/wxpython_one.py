#!/usr/bin/env python
import wx

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
Frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
Frame.Show(True)     # Show the frame.
app.MainLoop()





