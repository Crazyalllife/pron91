#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Liangmingli'
import os


##Linux in bytes预留500MB空间给服务器
MaxFreeSize = 1002400*500


def getCapacity():
    disk = os.statvfs("/")
    capacity = disk.f_bsize * disk.f_blocks
    return capacity

def getAvaiableSize():
    disk = os.statvfs("/")
    available = disk.f_bsize * disk.f_bavail
    available = available - MaxFreeSize
    return available

def getUsedSize():
    disk = os.statvfs("/")
    used = disk.f_bsize * (disk.f_blocks - disk.f_bavail)

    return used


def convertToKB( value):
    return value/1024

def convertToMB(value):

    return value/1.048576e6

def convertToGb(value):
    return value/1.073741824e9


def isDiskHasSpace(byteValue):

    avaiable = getAvaiableSize()
    if avaiable >= byteValue:

        return True
    else:
        return False

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size



BaseDownloadPath = "video/"

size = get_size(start_path=BaseDownloadPath)
print(size)

print(convertToGb(size))

