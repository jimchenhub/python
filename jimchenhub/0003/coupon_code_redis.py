#!/usr/bin/env python
#-*- encoding:utf-8 -*-
'''
save coupon code into redis
'''
import redis

config = {
    "host":'localhost', 
    "port":6379, 
    "db":0
    }

class Save_to_redis:
    def __init__(self, code_file, config):
        self.code_file = code_file
        self.config = config

    def connect_db(self):
        self.r = redis.Redis(host=self.config["host"], port = self.config["port"], db=self.config["db"])

    def save_code_to_redis(self):
        f = open("./coupon.txt")
        for code in f:
            code = code.strip('\n')
            self.r.rpush("coupon_list", code)
        f.close()

    def show_code_list(self):
        print self.r.lrange("coupon_list", 0, -1)

    def cleanup(self):
        while self.r.llen("coupon_list") :
            self.r.lpop("coupon_list")

def main():
    code_file = "./coupon.txt"
    redis = Save_to_redis(code_file, config)
    redis.connect_db()
    redis.save_code_to_redis()
    redis.show_code_list()
    redis.cleanup()

if __name__=="__main__":
    main()