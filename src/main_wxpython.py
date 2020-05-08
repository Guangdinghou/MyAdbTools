#!/usr/bin/python3

# -*- coding: UTF-8 -*-
import wx


class MainActivity(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()
        # 这里先创建列表项目，然后再绑定到对应的 File 按钮中。
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_ABORT, u'about', u'some infrmation about this app')
        file_menu.AppendSeparator()
        file_menu.Append(wx.ID_EXIT, u'exit', u'click to exit app')

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, u'File')
        self.SetMenuBar(menu_bar)
        self.Show()


app = wx.App()
win = MainActivity(None, "test wx")
app.MainLoop()
