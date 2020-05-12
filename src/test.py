import os

import wx
from src.base import Constants
# 导入mywin.py中内容


# 创建mainWin类并传入mywin.MyFrame1
from src.beans.device_info import DeviceInfo
from src.widget import wfform_main


# wxFormBuilder生成UI框架
class mainWin(wfform_main.RootFrame):
    device_list = []
    app_list = []

    def doShell(self, shell):
        self.tv_out.AppendText(shell)
        self.tv_out.AppendText("\n")

    def makeText(self, shell):
        content = ''
        if self.choice_device.GetSelection() != -1:
            content = ' -s ' + self.device_list[self.choice_device.GetSelection()]
        shell = shell % content;
        return shell
    def on_text_change_listener(self,event):
        index=self.m_notebook1.GetSelection()
        print('index:'+index)
    # 实现Button控件的响应函数showMessage
    def on_app_refresh(self, event):
        shell = self.makeText(Constants.adb_get_apps);
        result = os.popen(shell).readlines()
        self.app_list.clear()
        self.doShell(shell)
        self.cb_package_name.Clear()
        for line in result:
            self.doShell(line)
            package_name = line.replace("package:", '').replace('\n', '')
            if len(package_name) > 0:
                self.app_list.append(package_name)
                self.cb_package_name.Append(package_name)

    def on_device_refresh(self, event):
        print('hello')
        shell = Constants.adb_devices
        result = os.popen(Constants.adb_devices).readlines()
        self.tv_out.Clear()
        self.device_list.clear()
        self.choice_device.Clear()
        self.doShell(shell)
        for line in result:
            self.tv_out.AppendText(line)
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
                    self.choice_device.Append(split[0])
                if len(line) > 0:
                    self.SetStatusText(line)
        if self.choice_device.GetColumns() > 0:
            self.choice_device.SetSelection(0)
    def on_shell_select(self,event):
        print('hhh')

if __name__ == '__main__':
    # 下面是使用wxPython的固定用法
    app = wx.App()
    main_win = mainWin(None)

    main_win.Show()
    app.MainLoop()
