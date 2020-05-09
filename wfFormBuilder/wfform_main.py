# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class RootFrame
###########################################################################

class RootFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 686,359 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer1.SetMinSize( wx.Size( 300,300 ) )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bsizer_device_choice = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"选择设备", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bsizer_device_choice.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choice_deviceChoices = []
		self.choice_device = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_deviceChoices, 0 )
		self.choice_device.SetSelection( 0 )
		bsizer_device_choice.Add( self.choice_device, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.refresh_device = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		bsizer_device_choice.Add( self.refresh_device, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer2.Add( bsizer_device_choice, 0, wx.EXPAND, 5 )

		m_radioBox2Choices = [ u"输入文字", u"快捷命令", u"自由命令", u"自定义" ]
		self.m_radioBox2 = wx.RadioBox( self, wx.ID_ANY, u"选择功能", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox2.SetSelection( 0 )
		bSizer2.Add( self.m_radioBox2, 0, wx.ALL, 5 )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		bSizer2.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button2, 0, wx.ALIGN_CENTER, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		wSizer1.SetMinSize( wx.Size( 100,-1 ) )
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		wSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( wSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.refresh_device.Bind( wx.EVT_BUTTON, self.refresh_device )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def refresh_device( self, event ):
		event.Skip()


