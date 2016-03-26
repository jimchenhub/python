#! /usr/bin/env python
#-*- encoding: utf-8 -*-

import re

def count_words_num(file_name):
    f = open(file_name, "rb")
    content = f.read()
    words = re.findall(r"[a-zA-Z0-9]+", content)
    return len(words)

if __name__=='__main__':
    file_name = "./content.txt"
    print count_words_num(file_name)