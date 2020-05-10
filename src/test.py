import os

import wx

# 导入mywin.py中内容


# 创建mainWin类并传入mywin.MyFrame1
from src.beans.device_info import DeviceInfo
from src.widget import wfform_main

# wxFormBuilder生成UI框架
class mainWin(wfform_main.RootFrame):
    device_list = []


    # 实现Button控件的响应函数showMessage
    def on_device_refresh(self, event):
        print('hello')
        result = os.popen("adb devices").readlines()

        self.tv_out.Clear()
        self.device_list.clear()
        self.choice_device.Clear()
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


if __name__ == '__main__':
    # 下面是使用wxPython的固定用法
    app = wx.App()
    main_win = mainWin(None)

    main_win.Show()
    app.MainLoop()
