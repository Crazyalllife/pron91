#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sqlite3
"""
数据库部分
"""

class Databasemanager:
    def __init__(self):

        self.conn = sqlite3.connect('pron91.db')

        self.c = self.conn.cursor()
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

    def updatePronDownloadStatus(self,viewkey,status):

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