#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pron91pkg import httputil
from bs4 import BeautifulSoup



def handleXVideoContent(url):
    content = httputil.fetchContent(url)

    # print(content)

    soup = BeautifulSoup(content , "html.parser")
    results = soup.find_all("script")

    # print(len(results))

    result = None
    for one in results:

        strData = str(one)
        if 'html5player.setVideoUrl' in strData:
            print("find it")
            result = strData
    return result

def findUrl(result, field):


    ##前缀
    loc = result.find(field) +len(field) +len("('")
    result = result[loc:]
    ##后缀
    loc = result.find("');")


    result = result[:loc]

    return result


def findVideoType(url):
    right = url.find("?")
    left=url.rfind(".")
    type = url[left:right]
    return type


url = 'https://www.xvideos.com/video32351195/chinese_'
url = 'https://www.xvideos.com/video30319763/chinese_china_'

result = handleXVideoContent(url)


downloadUrl = findUrl(result,"setVideoUrlHigh")
print(downloadUrl)

title = findUrl(result,"setVideoTitle")
print(title)


type = findVideoType(downloadUrl)

print(type)