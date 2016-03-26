#!/usr/bin/env python
#-*- encoding: utf-8 -*-
'''
0009:一个HTML文件，找出里面的链接。
'''
import urllib2
from bs4 import BeautifulSoup

def show_href(url):
    content = urllib2.urlopen(url).read()

    soup = BeautifulSoup(content, "html.parser")
    for tag in  soup.find_all('a'):
        print tag['href']


if __name__ == '__main__':
    show_href('https://github.com/Yixiaohan/show-me-the-code')
