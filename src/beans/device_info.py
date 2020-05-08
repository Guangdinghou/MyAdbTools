#!/usr/bin/python3

# -*- coding: UTF-8 -*-
class DeviceInfo(object):


    def __init__(self, device_id, device_name, device_status):
        self.device_id = device_id
        self.device_name = device_name
        self.device_status = device_status

    def get_id(self):
        return self.device_id

    def get_name(self):
        return self.device_name

    def get_status(self):
        return self.device_status
