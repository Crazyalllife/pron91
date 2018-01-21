#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sqlite3
import os
"""
数据库部分
"""

class Databasemanager:
    def __init__(self):

        targetPath = 'spiderDB'
        try:
            os.makedirs(targetPath,0o0755);
        except FileExistsError:
            pass

        self.conn = sqlite3.connect('spiderDB/pron91.db' ,timeout=30)
        self.mode_wal = 'PRAGMA journal_mode=WAL'
        self.mode_rollback = 'PRAGMA journal_mode=DELETE'

        self.c = self.conn.cursor()
        #开启WAL模式
        self.c.execute(self.mode_wal)
        self.c.execute('''
        CREATE TABLE if not exists Pron
            (_id INTEGER          PRIMARY KEY     autoincrement,
            viewkey           TEXT    NOT NULL,
            title              text   ,
            time               text   ,
            sourceType         text   ,
            originalURL        text   ,
            actDownloadURL     text   ,
            downloadStatus     int);
            ''')

        self.c.execute('''
        CREATE TABLE if not exists Page
            (_id INTEGER          PRIMARY KEY     autoincrement,

            pageSize INT,
            pageIndex INT);
            ''')




        self.conn.commit()

        return



    def isPronExist(self,pron):

        viewkey = pron['viewkey']

        self.c = self.conn.cursor()
        cursor = self.c.execute("SELECT *  from Pron where viewkey=(?)",(viewkey,))

        length = len(cursor.fetchall())

        isExist = False
        if length > 0:
            isExist = True

        return isExist



    def insertPron(self,pron):

        pronData = [pron['viewkey'],pron['title'],pron['type'] ,pron['originalURL'],pron['actDownloadURL'],pron['downloadStatus']]

        self.c.execute("INSERT INTO Pron (viewkey,title,sourceType,originalURL,actDownloadURL,downloadStatus)\
        VALUES (?,?,?,?,?,?)" , pronData);

        self.conn.commit()

        return



    def updatePron(self,pron):


        pronData = [pron['title'],pron['type'] ,pron['originalURL'],pron['actDownloadURL'],pron['downloadStatus'],pron['viewkey']]

        self.c.execute("UPDATE Pron set  title=? , sourceType=?,originalURL=?,actDownloadURL=?,downloadStatus=? where viewkey=? " , pronData)
        self.conn.commit()

        return

    def insertOrUpdatePron(self,pron):

        value = self.isPronExist(pron)

        if value :
            self.updatePron(pron)
        else:
            self.insertPron(pron)

        return

    def getPronToDownload(self):
        cursor = self.c.execute("SELECT * from Pron WHERE downloadStatus=0 LIMIT 1")
        rows = cursor.fetchall()

        size = len(rows)

        if size > 0:

            for row in rows:
                _id = row[0]
                targetURL = row[5]
                viewkey = row[1]


            result = {
                "_id":_id,
                "viewkey":viewkey,
                "targetURL":targetURL
            }
        else:
            result = None
        return result

    def getLastPron(self):
        cursor = self.c.execute("SELECT * from Pron WHERE downloadStatus=0  ORDER BY _id DESC limit 1")
        rows = cursor.fetchall()

        size = len(rows)

        if size > 0:

            for row in rows:
                _id = row[0]
                targetURL = row[5]
                viewkey = row[1]


            result = {
                "_id":_id,
                "viewkey":viewkey,
                "targetURL":targetURL
            }
        else:
            result = None
        return result


    def updatePronDownloadStatus(self,viewkey,status):
        pronData = [status,viewkey]

        self.c.execute("UPDATE Pron set downloadStatus=? where viewkey=? " , pronData)
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


    def getDBPageSize(self):
        cursor = self.c.execute("SELECT *  from Page")
        rows = cursor.fetchall()

        for row in rows:
            pageSize = row[1]

        return pageSize


    def getDBPageIndex(self):
        cursor = self.c.execute("SELECT *  from Page")
        rows = cursor.fetchall()

        for row in rows:
            pageIndex = row[2]

        return pageIndex

    def getDBPath(self):

        cur = self.conn.cursor()
        cur.execute("PRAGMA database_list")
        rows = cur.fetchall()

        for row in rows:
            path = row[2]

        return path