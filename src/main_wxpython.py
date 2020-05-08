#!/usr/bin/python3

# -*- coding: UTF-8 -*-
import wx


class MainActivity(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # self.CreateStatusBar()
        # 这里先创建列表项目，然后再绑定到对应的 File 按钮中。
        file_menu = wx.Menu()
        menu_refresh = file_menu.Append(wx.ID_REFRESH, '刷新设备', 'click here to refresh device')

        file_menu.AppendSeparator()
        file_menu.Append(wx.ID_EXIT, u'exit', u'click to exit app')
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, u'File')

        # menu_refresh = wx.MenuBar()
        # menu_refresh.Append(null,u'refresh')
        self.SetMenuBar(menu_bar)
        self.Bind(wx.ID_REFRESH, self.OnClick)
        self.Show()

    def OnClick(self, e):
        print('123123')


app = wx.App()
win = MainActivity(None, "test wx")
app.MainLoop()
