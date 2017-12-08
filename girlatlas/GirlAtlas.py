
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Liangmingli'
import logging
from pron91pkg import httputil
import requests
from bs4 import BeautifulSoup
import re
import os
import shutil
from pron91pkg.FakeHeader import FakeHeader
BaseDownloadPath = "GirlAtlas/"

class GirlAtlas:
    def __init__(self , enter_point='https://www.girl-atlas.com'):

        logging.debug("Pron91 init")

        self.enter_point = enter_point


    def fetchMaxPageNumber(self ,url='https://www.girl-atlas.com/index1'):

        logging.debug("fetchMaxPageNumber")

        rawHtml = httputil.fetchContent(url)

        soup = BeautifulSoup(rawHtml , "html.parser")

        target = soup.find_all("ul",class_="pagination")
        target = target[0].find_all("li")


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
            print(id)
            print(title)


            picNumber =self.reRemove("含","张",albumContent.text)

            picNumber = int(picNumber)
            print(picNumber)
            author = self.reRemove("由","在",albumContent.text)


            print(author)

            date = self.reRemove("在","创",albumContent.text)
            watchTimes = self.reRemove("了","次",albumContent.text)

            albumURL = "https://www.girl-atlas.com/album/" + id + "?display=2"
            print(date)
            print(watchTimes)

            print(albumURL)
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
        rawHtml = httputil.fetchContent(url)
        soup = BeautifulSoup(rawHtml , "html.parser")
        targets = soup.find_all("ul",class_="gridview")
        targets = targets[0].find_all("li")

        print(len(targets))

        urls = []
        for target in targets:

            content = target.find("a")['href']
            urls.append(content)

        return urls

    def downloadAlbum(self , title , fileName,url):
        targetPath = BaseDownloadPath

        try:
            os.makedirs(targetPath,0o0755);
        except FileExistsError:
            print("下载目录存在")

        targetPath = targetPath + title

        try:
            os.makedirs(targetPath,0o0755);
        except FileExistsError:
            print("相册目录存在")


        left = url.rfind('.')
        rght = url.rfind('!')

        type = url[left:rght]
        #下载前先删除旧的同名图片
        targetPath = targetPath + "/"+str(fileName) +type
        try:
            os.remove(targetPath)
        except FileNotFoundError:
            print("")

        fakerHeader = FakeHeader()
        request_headers = fakerHeader.buildFakeHeader()
        # Upgrade-Insecure-Requests:1
        header =  {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36', 'Upgrade-Insecure-Requests': str(1)}
        print('request:' +request_headers)
        response = requests.get(url, stream=True ,headers=request_headers)


        with open(targetPath, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            del response

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
# ob.downloadAlbum("test",1,'https://girlatlas.b0.upaiyun.com/4/20121220/14253591da6584f21dee.jpg!lrg')

