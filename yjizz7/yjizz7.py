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
basePath = "Spider/yjizz7/"

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


url = "http://www.yjizz7.com/10461/%E7%88%B8%E7%88%B8%E4%B8%8D%E8%A6%81%E4%BA%86-%E7%9F%AD%E5%8F%91%E6%B0%94%E8%B4%A8%E5%B0%91%E5%A6%87%E8%A2%AB%E5%A4%A7%E9%B8%A1%E5%B7%B4%E5%B9%B2%E7%88%B9%E5%B9%B2%E5%88%B0%E5%8F%97%E4%B8%8D%E4%BA%86%E6%B1%82%E9%A5%B6/"
getVideoDownloadAddress(url)

# print(targetResult)
# httputil.downloadFile(targetResult['url'],targetResult['title'],targetResult['type'],"")