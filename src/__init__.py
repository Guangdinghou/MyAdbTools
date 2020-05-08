#!/usr/bin/python3

# -*- coding: UTF-8 -*-

import tkinter
import os

error = '没有连接的设备，请重试'


def on_click():
    result = os.popen("adb devices").readlines()
    print(len(result))
    if len(result) == 2:
        tab['text'] = error

    for line in result:
        print(line)
    # str.replace(result, "\\t", "   ")
    # print(result)


top = tkinter.Tk(className='adb tools')
top.geometry('500x500')
# tags
tab = tkinter.Label(top)
tab['text'] = '功能'
tab.pack()

button = tkinter.Button(top)
button['text'] = '刷新adb设备'
button['command'] = on_click
button.pack(side=tkinter.RIGHT)

top.mainloop()
