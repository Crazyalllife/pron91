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


url = "http://www.selaoban2.com/803/96%E5%B9%B4%E7%AB%A5%E9%A2%9C%E5%B7%A8%E4%B9%B3%E5%A4%84%E5%A5%B3%E7%AC%AC%E4%B8%80%E6%AC%A1%E5%8F%A3%E4%BA%A4%E5%BC%80%E6%88%BF-%E9%9D%9E%E5%B8%B8%E7%9A%84%E6%B0%B4%E5%AB%A9-%E5%A5%B3%E7%A5%9E%E9%A2%9C%E5%80%BC/"

url="http://www.selaoban2.com/recent/2/"
getVideoDownloadAddress(url)

# print(targetResult)
# httputil.downloadFile(targetResult['url'],targetResult['title'],targetResult['type'],"")