#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'Liangmingli'
from girlatlas.GirlAtlas import GirlAtlas
from girlatlas.GirlAtlasDataBase import DatabaseManager
import time
from pron91pkg import httputil
import traceback
import sys, os
from time import gmtime, strftime


def main():
    ob = GirlAtlas()
    db = DatabaseManager()
    album = db.getAlbumToDownload()
    running = True

    print(album)
    while(running and album != None):
        albumID = album['albumID']
        targetURL = album['targetURL']
        title = album['title']
        picURLs = ob.fetchAlbum(targetURL)

        num = 1
        print(title + '相册有' + str(len(picURLs)) + '张图片')

        for picURL in picURLs:
            print("开始下载：" +picURL)
            ob.downloadAlbum(title,str(num),picURL)
            num = num+1
        print('---------------相册下载完成')
        db.updateAlbumDownloadStatus(1,albumID)
        album = db.getAlbumToDownload()
    print()

def generateLogPath():

    pathName = os.path.dirname(sys.argv[0])

    strTime = strftime("%Y-%m-%d %H-%M-%S", gmtime())

    directory = pathName + "/crash/"
    logFilePath =  directory + strTime+"log.txt"

    if not os.path.exists(directory):
        os.makedirs(directory)
    return logFilePath


if __name__ == '__main__':
    logFilePath = generateLogPath()
    #This line opens a log file
    log = open(logFilePath, "w")
    try:

        main()
        # if AmIRunning():
        #     print("I am Running")
        # else:
        #     main()



    except Exception:
        traceback.print_exc(file=log)
