#!/usr/bin/env python
#-*- encoding:utf-8 -*-
'''
save coupon code into mysql database
'''
import random
import string
import MySQLdb

config = {
    "host":'localhost',
    "port" : 3306,
    "user":'root',
    "passwd":'jim',
    "db" :'python'
    }

class Save_to_mysql:
    def __init__(self, code_file, config):
        self.code_file = code_file
        self.config = config

    def connect_db(self):
        try:
            conn= MySQLdb.connect(host=self.config["host"], port=self.config["port"], user=self.config["user"], passwd=self.config["passwd"], db=self.config["db"])
        except MySQLdb.Error, e:
            try:  
                sqlError =  "Error %d:%s" % (e.args[0], e.args[1]) 
                print sqlError 
            except IndexError:  
                print "MySQL Error:%s" % str(e) 
        self.conn = conn
        self.cur = conn.cursor()

    def save_code_into_db(self):
        f = open("./coupon.txt")
        for code in f:
            print code
            sql = "insert into coupon_code(code) values('"+code+"')"
            print sql
            try:
                self.cur.execute(sql)
            except MySQLdb.Error, e:
                try:
                    sqlError =  "Error %d:%s" % (e.args[0], e.args[1]) 
                    print sqlError 
                except IndexError:  
                    print "MySQL Error:%s" % str(e)
        f.close()
        self.cur.close()
        self.conn.commit()
    def close_all(self):
        self.conn.close()

def main():
    code_file = "./coupon.txt"
    mysql = Save_to_mysql(code_file, config)
    mysql.connect_db()
    mysql.save_code_into_db()
    mysql.close_all()

if __name__=="__main__":
    main()