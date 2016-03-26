#!/usr/bin/env python
#-*- encoding:utf-8 -*-
'''
生成长度为10的唯一优惠码，由数字和字母组成
id + L + 随机码
'''
import random
import string

def generate_code(id, length=10):
    prefix = hex(int(id))[2:] + "L"
    length = length - len(prefix)
    chars=string.ascii_letters+string.digits
    return prefix + ''.join([random.choice(chars) for i in range(length)])
def main():
    for i in range(20):
        code = generate_code(i)
        print code

if __name__=="__main__":
    main()