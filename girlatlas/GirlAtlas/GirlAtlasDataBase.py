#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Liangmingli'


import sqlite3
import os

class DatabaseManager:
    def __init__(self):

        targetPath = 'spiderDB'
        try:
            os.makedirs(targetPath,0o0755);
        except FileExistsError:
            pass

        self.conn = sqlite3.connect('spiderDB/GirlAtlas.db' ,timeout=30)

        self.mode_wal = 'PRAGMA journal_mode=WAL'
        self.mode_rollback = 'PRAGMA journal_mode=DELETE'



        self.c = self.conn.cursor()
        #开启WAL模式
        self.c.execute(self.mode_wal)

        self.c.execute('''
        CREATE TABLE if not exists Page
            (_id INTEGER          PRIMARY KEY     autoincrement,

            pageSize INT default 0,
            pageIndex INT default 1);
            ''')

        self.c.execute('''
        CREATE TABLE if not exists Album
            (_id INTEGER          PRIMARY KEY     autoincrement,

            albumID TEXT    NOT NULL,
            albumTitle TEXT,
            picNumber integer,
            author text,
            albumDate text,
            watchTime integer,
            pageUrl text,
            downloadStatus integer
            );
            ''')
        self.c.execute('''
            CREATE TABLE if not exists Pictures
            (_id INTEGER          PRIMARY KEY     autoincrement,

            albumID TEXT    NOT NULL,
            url text,
            downloadStatus integer
            );
            ''')



        self.conn.commit()

    def isAlbumExist(self,albumId):

        self.c = self.conn.cursor()
        cursor = self.c.execute("SELECT *  from Album where albumID=(?)",(albumId,))

        length = len(cursor.fetchall())

        isExist = False
        if length > 0:
            isExist = True

        return isExist


    def insertAlbum(self , album):

        albumData = [album['albumId'],
                     album['title'],
                     album['picNumber'] ,
                     album['author'],
                     album['date'],
                     album['watchTimes'],
                     album['albumURL'],
                     -1]

        self.c.execute("INSERT INTO Album (albumID,albumTitle,picNumber,author,albumDate,watchTime,pageUrl,downloadStatus)\
        VALUES (?,?,?,?,?,?,?,?)" , albumData);

        self.conn.commit()
        return


    def updateAlbum(self,album , downloadStatus):
        albumData = [album['title'],
                     album['picNumber'] ,
                     album['author'],
                     album['date'],
                     album['watchTimes'],
                     album['albumURL'],
                     downloadStatus,
                    album['albumId']]
        self.c.execute("UPDATE Album set  albumTitle=? , picNumber=?,author=?,albumDate=?,watchTime,pageUrl,downloadStatus=? where albumId=? " , albumData)
        self.conn.commit()

        return



    def updatePageSize(self,size):


        cursor = self.c.execute("SELECT *  from Page")

        length = len(cursor.fetchall())

        isExist = False
        if length > 0:
            isExist = True

        if isExist:
            self.c.execute("UPDATE Page set pageSize="+str(size) + ";")
        else:
            self.c.execute("INSERT INTO Page (pageSize,pageIndex) VALUES ('" +str(size) + "',"
                  +"'" + "0'" +

                  ")");

        self.conn.commit()
        return


    def updatePageIndex(self , index):

        cursor = self.c.execute("SELECT *  from Page")

        length = len(cursor.fetchall())

        isExist = False
        if length > 0:
            isExist = True

        if isExist:
            self.c.execute("UPDATE Page set pageIndex=?" , (index,))
        else:
            self.c.execute("INSERT INTO Page (pageSize,pageIndex) VALUES (?,?)",(index,index))
        self.conn.commit()
        return


    def isPictureExist(self , url):
        self.c = self.conn.cursor()
        cursor = self.c.execute("SELECT *  from Pictures where url=(?)",(url,))

        length = len(cursor.fetchall())

        isExist = False
        if length > 0:
            isExist = True

        return isExist

    def insertPicture(self , albumID , url):

        self.c.execute("INSERT INTO Pictures (albumID,url,downloadStatus)\
        VALUES (?,?,?)" , (albumID,url,0));

        self.conn.commit()

        return

    def updatePicture(self,url ,downloadStatus):

        self.c.execute("UPDATE Pictures set  downloadStatus=? where url=? " , (downloadStatus,url))
        self.conn.commit()

        return


    def getDBPageIndex(self):
        cursor = self.c.execute("SELECT *  from Page")
        rows = cursor.fetchall()

        for row in rows:
            pageIndex = row[2]

        return pageIndex

    def getAlbumToDownload(self):
        cursor = self.c.execute("SELECT * from Album WHERE downloadStatus=-1 LIMIT 1")
        rows = cursor.fetchall()

        size = len(rows)

        if size > 0:

            for row in rows:
                titleKey = row[0]
                targetURL = row[7]
                viewkey = row[1]
                title = row[2]

            result = {
                "albumID":viewkey,
                "targetURL":targetURL,
                "title":title,
                "titleKey":titleKey
            }
        else:
            result = None
        return result

    def updateAlbumDownloadStatus(self,status,albumID):
        self.c.execute("UPDATE Album set  downloadStatus=? where albumID=? " , (status,albumID))
        self.conn.commit()
        return

    def isPictureDownloaded(self,url):
        result = False
        cursor = self.c.execute("SELECT * from Pictures WHERE url=? and downloadStatus = 1",(url,))

        length = len(cursor.fetchall())
        print("是否下载？"+url)
        if length > 0:
            result = True
        return result