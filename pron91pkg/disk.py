#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Liangmingli'
import os


##Linux in bytes
MaxFreeSize = 500


def getCapacity():
    disk = os.statvfs("/")
    capacity = disk.f_bsize * disk.f_blocks
    return capacity

def getAvaiableSize():
    disk = os.statvfs("/")
    available = disk.f_bsize * disk.f_bavail
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



