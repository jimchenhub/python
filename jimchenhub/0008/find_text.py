#!/usr/bin/env python
#-*- encoding: utf-8 -*-
'''
0008:一个HTML文件，找出里面的正文。
'''
import urllib2
from bs4 import BeautifulSoup

def find_text_in_html(url):
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "html.parser")
    for string in soup.stripped_strings:
        print string

if __name__=="__main__":
    url = "https://github.com/Yixiaohan/show-me-the-code"
    find_text_in_html(url)