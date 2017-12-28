#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from pron91pkg import httputil
from bs4 import BeautifulSoup
from pron91pkg import disk
import requests
import shutil
import os
import time
from pron91pkg.FakeHeader import FakeHeader

Sleep_Per_File = 0
Sleep_Per_TioutOut = 10
chunk_size = 512
basePath = "Spider/auto25/"

"""
1.找cotent
2。找title
3。找视频下载地址
"""


def getVideoDownloadAddress(url):

    content = httputil.fetchContent(url)
    print(content)

    soup = BeautifulSoup(content , "html.parser")
    results = soup.find_all("title")

    title = results[0].text

    results = soup.find_all("video",class_="video-js vjs-default-skin")
    tag = results[0]
    ones = tag.find_all("source")

    hight = 0

    targetUrl = ""

    for one in ones:
        print(one['res'])
        print(one['src'])

        oneLevelStr = one['res']

        oneLevel = int(oneLevelStr)

        if oneLevel > hight:
            hight = oneLevel
            targetUrl = one['src']

    index = targetUrl.rfind(".")
    type = targetUrl[index:]
    targetResult = {
        "title":title,
        "url":targetUrl,
        "type":type
    }
    return targetResult




url="http://www.aotu26.com/13535/%E5%AE%BE%E9%A6%86%E5%BC%80%E6%88%BF%E5%B0%91%E5%A5%B3%E7%9A%84%E9%80%BC%E6%AF%9B%E8%8C%82%E5%AF%86%E6%80%A7%E6%AC%B2%E5%BC%BA%E5%98%B4%E9%87%8C%E8%AF%B4%E4%B8%8D%E8%A6%81%E4%B8%8B%E9%9D%A2%E5%A4%B9%E7%9D%80%E9%B8%A1%E5%B7%B4%E4%B8%8D%E6%94%BE/"

targetResult = getVideoDownloadAddress(url)

print(targetResult)
httputil.downloadFile(targetResult['url'],targetResult['title'],targetResult['type'],"")