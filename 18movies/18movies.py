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

    # soup = BeautifulSoup(content , "html.parser")
    # results = soup.find_all("title")
    #
    # title = results[0].text
    #
    # results = soup.find_all("video",class_="video-js vjs-default-skin")
    # tag = results[0]
    # ones = tag.find_all("source")
    #
    # hight = 0
    #
    # targetUrl = ""
    #
    # for one in ones:
    #     print(one['res'])
    #     print(one['src'])
    #
    #     oneLevelStr = one['res']
    #
    #     oneLevel = int(oneLevelStr)
    #
    #     if oneLevel > hight:
    #         hight = oneLevel
    #         targetUrl = one['src']
    #
    # index = targetUrl.rfind(".")
    # type = targetUrl[index:]
    # targetResult = {
    #     "title":title,
    #     "url":targetUrl,
    #     "type":type
    # }
    # return targetResult


url="https://www.18movies.club/archives/category/av%E8%A7%86%E9%A2%91"
getVideoDownloadAddress(url)

# print(targetResult)
# httputil.downloadFile(targetResult['url'],targetResult['title'],targetResult['type'],"")