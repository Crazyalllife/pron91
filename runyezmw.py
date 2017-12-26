#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Liangmingli'
from yezmw import yezmw


# url = "http://yezmw.com/video/show/id/4239"
url = "http://yezmw.com/video/show/id/1773"
print("解析页面内容")
#解析页面内容
result = yezmw.handleVideoContent(url)
#解析链接
print("解析链接")
lineCount = yezmw.decodeM3u8File(result["title"],result["hlsViedoUrl"])
#下载文件
print("下载文件")
yezmw.startdownloadVideo(url,result["title"],lineCount)
print("下载完成")