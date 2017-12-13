
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Liangmingli'
import logging
from pron91pkg import httputil
from bs4 import BeautifulSoup
import re
import os
import requests
from pron91pkg.FakeHeader import FakeHeader

BaseDownloadPath = "GirlAtlas/"

referer = 'https://www.girl-atlas.com'
class GirlAtlas:
    def __init__(self ,enter_point='https://www.girl-atlas.com'):

        logging.debug("Pron91 init")

        self.enter_point = enter_point
        self.fake = FakeHeader()


    def fetchMaxPageNumber(self ,url='https://www.girl-atlas.com/index1'):

        logging.debug("fetchMaxPageNumber")

        rawHtml = httputil.fetchContent(url)
        # print(rawHtml)
        soup = BeautifulSoup(rawHtml , "html.parser")

        targets = soup.find_all("ul",class_="pagination")

        size = len(targets)
        # print('size 是' + str(size))
        if size == 0:
            return 0
        target = targets[0].find_all("li")


        numbers = []
        isShowMaxPage = False
        for one in  target:
            oneContent = one.find("a")
            value = oneContent.text
            if ">" in value:
                print("----------->")
                isShowMaxPage = False
                continue

            if "(current)" in value:
                value =value.replace("(current)","")

            if "..." in value:
                continue

            value = value.strip()
            numbers.append(int(value))

        max = 0
        for number in numbers:
            if number > max:
                max = number


        return  max


    def fetchTargetPage(self,page=1):
        url = 'https://www.girl-atlas.com/index1?p=' + str(page)

        rawHtml = httputil.fetchContent(url)

        soup = BeautifulSoup(rawHtml , "html.parser")
        targets = soup.find_all("div",class_="album-item row")

        results = []
        for target in targets:
            print("-------------")
            idContent = target.find("h2")
            idContent = idContent.find("a")

            title = idContent.text
            id = idContent['href']
            id = id.replace("/album/","")

            albumContent = target.find("p",class_="desp")
            # print(id)
            # print(title)


            picNumber =self.reRemove("含","张",albumContent.text)

            picNumber = int(picNumber)
            # print(picNumber)
            author = self.reRemove("由","在",albumContent.text)


            # print(author)

            date = self.reRemove("在","创",albumContent.text)
            watchTimes = self.reRemove("了","次",albumContent.text)

            albumURL = "https://www.girl-atlas.com/album/" + id + "?display=2"
            # print(date)
            # print(watchTimes)

            # print(albumURL)
            print("标题:" + title + " 相册共" + str(picNumber) +"张 " + "地址:" + albumURL)
            result = {
                "albumId":id,
                "title":title,
                "picNumber":picNumber,
                "author":author,
                "date":date,
                "watchTimes":watchTimes,
                "albumURL":albumURL
            }
            results.append(result)
            print("-------------")


        return results



    def reRemove(self,start="", end="",origin=""):

        value = re.sub("[\s\S]*?"+start,"",origin)
        value = re.sub(end+"[\s\S]*?次","",value)
        value = value.replace("次","")
        value = value.strip()
        return value


    def fetchAlbum(self,url):
        urls = []
        rawHtml = httputil.fetchContent(url)
        soup = BeautifulSoup(rawHtml , "html.parser")
        contents = soup.find_all("ul",class_="gridview")
        if len(contents) == 0:
            return urls

        targets = contents[0].find_all("li")

        # print(len(targets))


        for target in targets:

            content = target.find("a")['href']
            urls.append(content)

        return urls

    def downloadAlbum(self , title , fileName,url):
        targetPath = BaseDownloadPath
        empty = None
        try:
            os.makedirs(targetPath,0o0755);
        except FileExistsError:
            empty = None

        targetPath = targetPath + title

        try:
            os.makedirs(targetPath,0o0755);
        except FileExistsError:
            empty = None


        left = url.rfind('.')
        rght = url.rfind('!')

        type = url[left:rght]
        #下载前先删除旧的同名图片
        targetPath = targetPath + "/"+str(fileName) +type
        try:
            os.remove(targetPath)
        except FileNotFoundError:
            empty = None



        header = self.fake.buildFakeHeader(referer = referer)
        response = requests.get(url, verify=False,headers=header , timeout = 10)

        outFile = open(targetPath,'wb')
        outFile.write(response.content)
        outFile.close()
        del response

        print("图片OK")
        return
#
# ob = GirlAtlas()
#
#
#
#
#
# # print(ob.fetchTargetPage(885))
# urls = ob.fetchAlbum('https://www.girl-atlas.com/album/576545e258e039318beb3912?display=2')
# print(urls)
#
#

# fakerHeader = FakeHeader()
#
# request_headers = fakerHeader.buildFakeHeader()
# session = requests.Session()
# url = 'https://www.girl-atlas.com/album/576545e258e039318beb3912'
# html = session.get(url,allow_redirects=True,headers = request_headers ,verify=False)

# print(html.status_code)
# print(html.encoding)
# print(html.headers)
# # print(html.text)
# print(html.history)
# print(html.cookies)
# print(html.cookies.keys())
# print(html.cookies.values())

# url = 'https://girlatlas.b0.upaiyun.com/4/20121220/1426719b95af6976cdef.jpg!lrg'
# session.headers.update({'referer':'https://www.girl-atlas.com'})
# respone = requests.get(url ,verify=False,headers = {'referer':'https://www.girl-atlas.com'})
#
# print(respone.status_code)
# print(respone.encoding)
# print(respone.headers)
# print('---------------------')
#
# targetPath = '1.jpg'
# outFile = open(targetPath,'wb')
# outFile.write(respone.content)
# outFile.close()
