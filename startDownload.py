#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pron91pkg.pron91 import Pron91
from pron91pkg.databasemanager import Databasemanager
import time
from pron91pkg import httputil

running = True
SLEEP_per_Video = 10
if __name__ == '__main__':
    pron = Pron91();
    db = Databasemanager()


    targetPron = db.getPronToDownload()
    while (targetPron != None and running):

        url = targetPron['targetURL']
        viewkey = targetPron['viewkey']

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
            if isHaveSpace:
                db.updatePronDownloadStatus(viewkey,1)
                targetPron = db.getPronToDownload()
            else:
                running = False
        except:
            db.updatePronDownloadStatus(viewkey,0)


        time.sleep(SLEEP_per_Video)

    print("End")