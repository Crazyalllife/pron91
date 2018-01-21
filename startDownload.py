#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pron91pkg.pron91 import Pron91
from pron91pkg.databasemanager import Databasemanager
import time

import traceback
import sys, os
from time import gmtime, strftime
import subprocess
from pron91pkg.disk import get_size
from pron91pkg.disk import convertToGb
from pron91pkg import httputil

running = True
SLEEP_per_Video = 10
# 20GB
MAX_DOWNLOAD_SIZE = 20


# def AmIRunning():
#     out_bytes = subprocess.check_output('ps -ef | grep python3', shell=True)
#     text = out_bytes.decode('utf-8')
#     fileName = os.path.abspath(sys.argv[0])
#
#     if fileName in text:
#         return True
#     else:
#         return False

def main():
    pron = Pron91();

    db = Databasemanager()

    running = True
    targetPron = db.getPronToDownload()
    while (targetPron != None and running):

        url = targetPron['targetURL']
        viewkey = targetPron['viewkey']

        urll = httputil.convertURL(url)

        contentCheck = httputil.fetchContent(urll)

        isMiss = httputil.fetchIsVideoMiss(contentCheck)

        if isMiss == False :


            result = pron.fetch(url)
            downloadURL = result['downloadURL']
            title = result['title']
            type = result['type']

            pronData = {
                "viewkey":viewkey,
                "originalURL":url,
                "title":title,
                "type":type,
                "actDownloadURL":downloadURL,
                "downloadStatus":"0"
            }
            db.insertOrUpdatePron(pronData)

            print(result)

            file = title + "." + type


            try:

                isHaveSpace = httputil.downloadVideo(downloadURL,file)

                print("isHaveSpace" + str(isHaveSpace))
                if isHaveSpace:
                    db.updatePronDownloadStatus(viewkey,1)
                    targetPron = db.getPronToDownload()
                else:
                    running = False
            except:
                db.updatePronDownloadStatus(viewkey,0)

            foldersize = get_size(httputil.BaseDownloadPath)
            foldersize = convertToGb(foldersize)

            if foldersize > MAX_DOWNLOAD_SIZE:
                running = False
        else:
            #文件miss
            db.updatePronDownloadStatus(viewkey,2)

        time.sleep(SLEEP_per_Video)

    print("End")

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


