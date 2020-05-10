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

class RootFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(900, 650), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(500, 300), wx.DefaultSize)

        self.m_statusBar1 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menubar1.Append(self.m_menu1, u"File")

        self.SetMenuBar(self.m_menubar1)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer1.SetMinSize(wx.Size(300, 300))
        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer12.SetMinSize(wx.Size(-1, 400))
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bsizer_device_choice = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"选择设备", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        bsizer_device_choice.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        choice_deviceChoices = []
        self.choice_device = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_deviceChoices, 0)
        self.choice_device.SetSelection(0)
        bsizer_device_choice.Add(self.choice_device, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.btn_refresh_device = wx.Button(self, wx.ID_ANY, u"刷新设备", wx.DefaultPosition, wx.DefaultSize, 0)
        bsizer_device_choice.Add(self.btn_refresh_device, 0, wx.ALL, 5)

        bSizer2.Add(bsizer_device_choice, 0, wx.EXPAND, 5)

        bsizer_package_choice = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"包     名 ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)

        bsizer_package_choice.Add(self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        cb_package_nameChoices = []
        self.cb_package_name = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           cb_package_nameChoices, 0)
        bsizer_package_choice.Add(self.cb_package_name, 1, wx.ALL, 5)

        bSizer2.Add(bsizer_package_choice, 0, wx.EXPAND, 5)

        m_radioBox2Choices = [u"输入文字", u"快捷命令", u"自由命令", u"自定义"]
        self.m_radioBox2 = wx.RadioBox(self, wx.ID_ANY, u"选择功能", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices,
                                       1, wx.RA_SPECIFY_ROWS)
        self.m_radioBox2.SetSelection(0)
        bSizer2.Add(self.m_radioBox2, 0, wx.ALL, 5)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        bSizer2.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        bSizer12.Add(bSizer2, 1, wx.EXPAND, 5)

        self.btn_get_shell = wx.Button(self, wx.ID_ANY, u"生成命令", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.btn_get_shell, 0, wx.ALIGN_CENTER, 5)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        bSizer8.Add(self.m_textCtrl2, 1, wx.ALL | wx.EXPAND, 5)

        self.btn_do_shell = wx.Button(self, wx.ID_ANY, u"执行命令", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.btn_do_shell, 0, wx.ALL | wx.EXPAND, 5)

        bSizer12.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer12, 1, wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer1.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.tv_out = wx.StaticText(self, wx.ID_ANY, u"输出内容", wx.DefaultPosition, wx.DefaultSize, 0)
        self.tv_out.Wrap(-1)

        bSizer1.Add(self.tv_out, 0, wx.ALL, 5)

        self.tv_out = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), wx.TE_MULTILINE)
        self.tv_out.SetMinSize(wx.Size(-1, 200))

        bSizer1.Add(self.tv_out, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_refresh_device.Bind(wx.EVT_BUTTON, self.on_device_refresh, self.btn_refresh_device)
        self.btn_get_shell.Bind(wx.EVT_BUTTON, self.on_make_shell, self.btn_get_shell)
        self.btn_do_shell.Bind(wx.EVT_BUTTON, self.on_do_shell, self.btn_do_shell)
        self.m_notebook1.AddPage(tag_input(self.m_notebook1), "自定义")
        self.m_notebook1.AddPage(tag_fast(self.m_notebook1), "快捷方式")

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_device_refresh(self, event):
        event.Skip()

    def on_make_shell(self, event):
        event.Skip()

    def on_do_shell(self, event):
        event.Skip()


###########################################################################
## Class tag_input
###########################################################################

class tag_input(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        tag_container = wx.BoxSizer(wx.VERTICAL)

        self.tv_custom_input = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           wx.TE_MULTILINE)
        tag_container.Add(self.tv_custom_input, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(tag_container)
        self.Layout()

    def __del__(self):
        pass


###########################################################################
## Class tag_fast
###########################################################################

class tag_fast(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        tv_my_shellsChoices = [u"adb shell dumpsys activity activities | grep mFocusedActivity", u"3245423423",
                               u"123123124123"]
        self.tv_my_shells = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, tv_my_shellsChoices, 0)
        bSizer11.Add(self.tv_my_shells, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer11)
        self.Layout()

        # Connect Events
        self.tv_my_shells.Bind(wx.EVT_LISTBOX_DCLICK, self.on_shell_select)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_shell_select(self, event):
        event.Skip()
