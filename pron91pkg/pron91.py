#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
爬取91的基本功能
"""

import os
import logging
import time
from pron91pkg import httputil
#ip被限制的时候睡眠
IP_LIMIT_TIME = 10 * 60

class Pron91:
    def __init__(self , enter_point='http://91porn.com/index.php'):
        self._enter_point = enter_point

        logging.debug("Pron91 init")



    def fetch_home_page(self):
        """
        返回首页的视频链接
        :return:
        """
        self.fetchTargetPage(self._enter_point)

    def fetch(self,url):
        """
        获取指定链接下的视频链接
        :param url:
        :return:
        """

        while True :


            url = httputil.convertURL(url)
            content = httputil.fetchContent(url)


            # print(content)
            result = httputil.fetchActualMessage(content)

            if result != None :
                break
            else:
                print("sleep ")
                time.sleep(IP_LIMIT_TIME)

        return result


    def fetchTargetPage(self , url):
        """
        获取指定页面的视频link
        :return:
        """
        content = httputil.fetchContent(url)
        result = httputil.fecthActualPageMessage(content)

        return result


    def fetchPageNumber(self, num):
        """
        获取指定页码的视频详情页
        :param num:
        :return:
        """
        url = "http://91porn.com/v.php?&page=" + str(num)




        return self.fetchTargetPage(url)


    def fetchMaxPageNumber(self,url):
        """
        获取最大页码
        """
        global number
        global hasNextNavi
        global content

        content = httputil.fetchContent(url)
        hasNextNavi = httputil.isPageNaviHasNext(content)
        number = httputil.fetchMaxPageNumber(content)
        if hasNextNavi:


            number = number + 1
            # print("has" + str(hasNextNavi) + " number:" + str(number))
            #
            # url = "http://91.7h5.space/v.php?next=watch&page=" + str(number)
            # content = httputil.fetchContent(url)
            # # hasNextNavi = httputil.isPageNaviHasNext(content)
            # number = httputil.fetchMaxPageNumber(content)

        return number






