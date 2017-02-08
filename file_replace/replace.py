#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/8 9:55
# @Author  : Feng_xia
# @File    : replace.py
import sys,os

if len(sys.argv)<=4:
    print('usage:./replace.py old_text new_text filename [-bak]')
# old_text,new_text=sys.argv[1],sys.argv[2]
old_text,new_text='2009','cctv'
# file_name=sys.argv[3]
file_name='/learn_python/learn_python/file_replace/1.txt'

f = open(file_name,'rb')
new_file=open('%s.bak'% file_name,'wb')
for line in f:
    new_file.write(line.decode().replace(old_text,new_text).encode())
f.close()
new_file.close()


