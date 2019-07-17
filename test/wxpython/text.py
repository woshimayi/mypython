# wxpython 教程
# https://wiki.wxpython.org/Getting%20Started#Laying_out_Visual_Elements
# https://www.cnblogs.com/coderzh/archive/2008/11/23/1339310.html
# 



import wx
import os


class MyFrame(wx.Frame):

	def __init__(self, parent, title):
		self.dirname = ''

		wx.Frame.__init__(self, parent, title=title)
		# self.control  = wx.TextCtrl(self, pos=(400, 400),  size=(50, 50), style=wx.TE_MULTILINE)
		self.CreateStatusBar()

		# seting menubar
		filemenu = wx.Menu()
		menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open a file to edit")
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
		menuExit =  filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")
		
		# createing the menubar 
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "&File")
		self.SetMenuBar(menuBar)
		
		# Event 
		self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)


		self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
		self.sizer2 = wx.BoxSizer(wx.VERTICAL)
		# self.buttons = []
		# for i in range(0, 6):
		# 	self.buttons.append(wx.Button(self, -1, "Button &" + str(i)))
		# 	self.sizer2.Add(self.buttons[i], 1, wx.Buttom)

		# use some sizer to see layout options
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		# self.sizer.Add(self.control, 1, wx.EXPAND)
		self.sizer.Add(self.sizer2, 0, wx.EXPAND)

		self.SetSizer(self.sizer)
		self.SetAutoLayout(True)
		self.sizer.Fit(self)
		self.Show(True)


	def OnAbout(self, e):
		dlg = wx.MessageDialog(self, "A small text, editor", "About sample Editor", wx.OK)
		dlg.ShowModal()
		dlg.Destroy()

	def OnExit(self, e):
		self.Close(True)

	def OnOpen(self, e):
		dlg = wx.FileDialog(self, "Choose a file ", self.dirname, "", "*.*", wx.FD_OPEN)
		if dlg.ShowModle() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			f = open(os.path.join(self.dirname, self.filename), 'r')
			self.control.SetValue(f.read())
			f.close()
		dlg.Destroy()



class ExampleGrame(wx.Panel):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, size=(700, 500))
		panel = wx.Panel(self)
		self.quote = wx.StaticText(panel, label='You quote:', pos=(20, 30))

		wx.StaticText(self, label='logger show', pos=(300, 4))
		self.logger = wx.TextCtrl(self, pos=(300, 20), size=(200, 300), style=wx.TE_MULTILINE | wx.TE_READONLY)
		
		# a button
		self.button = wx.Button(self, label="Save", pos=(200, 325))
		self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

		# the edit control one line version
		self.lblname = wx.StaticText(self, label="You name:", pos=(20, 30))
		self.editname = wx.TextCtrl(self, value="Enter here your name", pos=(150, 30), size=(140, -1))

		self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
		self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

		# the conbobox control 
		self.sampleList = ['firends', 'advertising', 'web search', 'Yellow Pages']
		self.lblhear = wx.StaticText(self, label="How did you hear form us ?", pos=(20, 90))
		self.edithear = wx.ComboBox(self, pos=(190, 90), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
		self.Bind(wx.EVT_COMBOBOX, self.EvtCombobox, self.edithear)
		self.Bind(wx.EVT_TEXT, self.EvtText,  self.edithear)

		# checkbox control
		self.insure = wx.CheckBox(self, label="Do you want Insure Shipment ?", pos=(20 ,180))
		self.Bind(wx.EVT_CHECKBOX, self.EvtCheckbox, self.edithear)

		# radio boxs 
		radioList = ['blue', 'red', 'yellow', 'orange', 'green', 'purple', 'navy blue', 'black', 'gray']
		rb = wx.RadioBox(self, label="What color would you like ?", pos=(20, 210), choices=radioList, majorDimension=3, style=wx.RA_SPECIFY_COLS)
		self.Bind(wx.EVT_RADIOBOX, self.EvtRadiobox, rb)
	
		self.Show()

	# Event functions
	def EvtRadiobox(self, event):
		self.logger.AppendText('EvtRadiobox :%d' % event.GetInt())

	def EvtCombobox(self, event):
		self.logger.AppendText('EvtCombobox :%s' % event.GetString())

	def OnClick(self, event):
		self.logger.AppendText('OnClick :%d' % event.GetId())
	
	def EvtText(self, event):
		self.logger.AppendText('EvtText :%s' % event.GetString())

	def EvtChar(self, event):
		self.logger.AppendText('EvtChar :%d' % event.GetKeyCode())

	def EvtCheckbox(self, event):
		self.logger.AppendText('EvtCheckbox :%d' % event.Checked())








app = wx.App(False)
frame = MyFrame(None, "edit")
panel = ExampleGrame(frame)
panel.Show()

app.MainLoop()