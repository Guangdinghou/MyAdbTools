#!/usr/bin/python3

# -*- coding: UTF-8 -*-
import os
import wx

from src.beans.device_info import DeviceInfo


class MainActivity(wx.Frame):
    device_list = []

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.panel = wx.Panel(parent=self)
        self.hbox1 = wx.BoxSizer()

        # self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()
        # 这里先创建列表项目，然后再绑定到对应的 File 按钮中。
        self.create_menu_bar()

        self.Show()

    def create_menu_bar(self):
        file_menu = wx.Menu()
        refresh_item = file_menu.Append(wx.ID_REFRESH, '刷新设备', 'click here to refresh device')
        file_menu.AppendSeparator()
        file_menu.Append(wx.ID_EXIT, u'exit', u'click to exit app')
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, u'File')
        # self.setCmobox()
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.on_click, refresh_item)

        # vbox.Add(hbox2, 1, flag=wx.ALL | wx.EXPAND, border=5)

    def refresh_devices(self):
        print('s')

    def on_click(self, e):
        result = os.popen("adb devices").readlines()
        print(type(result))
        self.device_list.clear()
        for line in result:
            if len(line) == 1:
                result.remove(line)
                continue
        if len(result) == 1:
            self.SetStatusText(u'没有链接设备')
        else:
            for line in result:
                deviceInfo = DeviceInfo('', '', '')
                print(line + "<<")
                line = str.replace(line, '\n', '')
                split = str.split(line, '\t')
                # unauthorized
                print(split)
                if len(split) == 2:
                    deviceInfo.device_id = split[0]
                    deviceInfo.device_status = split[1]
                    print(deviceInfo)
                    self.device_list.append(split[0])
                if len(line) > 0:
                    self.SetStatusText(line)
        self.setCmobox()

    def setCmobox(self):
        statictext = wx.StaticText(self.panel, label='选择目标设备：')
        self.ComboBox = wx.ComboBox(self.panel, -1, choices=self.device_list, style=wx.CB_SORT)
        self.hbox1.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        self.hbox1.Add(self.ComboBox, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        # 添加事件处理
        self.Bind(wx.EVT_COMBOBOX, self.on_combobox, self.ComboBox)
        if len(self.device_list) == 1:
            self.ComboBox.SetLabelText(self.device_list[0])
        self.panel.SetSizer(self.hbox1)
        pass

    def on_combobox(self, event):
        self.ComboBox.SetLabelText(event.GetString())
        print("选择{0}".format(event.GetString()))


app = wx.App()
win = MainActivity(None, "test wx")
app.MainLoop()
