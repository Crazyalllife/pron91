#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Liangmingli'
import os
import sys
import traceback
from time import gmtime, strftime
from pron91pkg.disk import get_size
from pron91pkg.disk import convertToGb
from pron91pkg import httputil
from girlatlas.GirlAtlas.GirlAtlas import GirlAtlas
from girlatlas.GirlAtlas.GirlAtlasDataBase import DatabaseManager
import time
MAX_DOWNLOAD_SIZE = 10

SLEEP_per_Album = 10
SLEEP_For_TimeOut = 60
def main():
    ob = GirlAtlas()
    db = DatabaseManager()
    album = db.getAlbumToDownload()
    running = True

    print(album)
    while(running and album != None):
        tilteKey = "["+str(album['titleKey'])+"]"
        albumID = album['albumID']
        targetURL = album['targetURL']
        title = album['title']
        picURLs = ob.fetchAlbum(targetURL)
        title = title + tilteKey

        num = 1
        print(title + '相册有' + str(len(picURLs)) + '张图片')

        for picURL in picURLs:

            if db.isPictureDownloaded(picURL):
                print( " 第"+ str(num) + "张"+"图片已经被下载")

                num = num+1
            else:

                print("开始下载：" +picURL + " 第"+ str(num) + "张")
                try:
                    ob.downloadAlbum(title,str(num),picURL)
                except(TimeoutError):
                    time.sleep(SLEEP_For_TimeOut)
                    continue
                num = num+1
                db.updatePicture(picURL,1)

        print('---------------相册下载完成')
        time.sleep(SLEEP_per_Album)
        foldersize = get_size(httputil.BaseDownloadPath)
        foldersize = convertToGb(foldersize)

        if foldersize > MAX_DOWNLOAD_SIZE:
            running = False
        else:

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
     main()
    # logFilePath = generateLogPath()
    # #This line opens a log file
    # log = open(logFilePath, "w")
    # try:
    #
    #     main()
    #     # if AmIRunning():
    #     #     print("I am Running")
    #     # else:
    #     #     main()
    #
    #
    #
    # except Exception:
    #     traceback.print_exc(file=log)
