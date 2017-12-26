#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Liangmingli'
import random
from fake_useragent import FakeUserAgent

class FakeHeader:
    """
    生成随机UserAgent
    生成随机IP
    """
    def __init__(self):
        self.ua = FakeUserAgent()
        self.language = 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4'
        self.accept = 'image/webp,image/apng,text/html,image/jpeg,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'

    def prepareip(self):

        """
        生成一个随机的IP
        :return:
        """
        randIP = str(random.randint(0, 255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))

        return randIP

    def buildFakeHeader(self ,referer = None):
        ip = self.prepareip()
        userAgent = self.ua.random
        if referer == None:

            request_headers = {
                "Accept-Language":self.language ,
                "User-Agent":userAgent ,
                "Accept":self.accept ,
                "X-Forwarded-For":ip
            }
        else:
            request_headers = {
            "Accept-Language":self.language ,
            "User-Agent":userAgent ,
            "Accept":self.accept ,
            "X-Forwarded-For":ip,
            "referer":referer,
            "X-Requested-With":"ShockwaveFlash/28.0.0.126",
            "Connection":"keep-alive",
            "Accept-Encoding": "gzip, deflate"
        }

        return request_headers

    def buildFakeHeaderWithCookie(self,cookie):
        ip = self.prepareip()
        userAgent = self.ua.random

        request_headers = {
            "Accept-Language":self.language ,
            "User-Agent":userAgent ,
            "Accept":self.accept ,
            "X-Forwarded-For":ip,
            "cookie":cookie,
            "Accept-Encoding":"gzip, deflate, br"
        }

        return request_headers




