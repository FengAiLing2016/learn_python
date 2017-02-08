#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/8 9:55
# @Author  : Feng_xia
# @File    : replace.py
import sys
import os

if len(sys.argv) <= 4:  #如果参数小于4个，提示输入参数
    print('usage:./replace.py old_text new_text filename [-bak]')
old_text, new_text = sys.argv[1], sys.argv[2]  #将参数 1 、2 赋予变量
file_name = sys.argv[3]     #将参数 3 赋予变量

f = open(file_name, 'r')    #以只读方式打开文件
new_file = open('%s.bak1' % file_name, 'w')     #以只写方式打开文件
for line in f:  #循环读取文件
    new_file.write(line.replace(old_text, new_text))    #循环写入改好的字符串
f.close()
new_file.close()
if '-bak' in sys.argv:  #有-bak参数的情况
    os.rename(file_name, '%s.bak' % file_name)
    os.rename('%s.bak1' % file_name, file_name)
else:
    os.remove('%s' % file_name)
    os.rename('%s.bak1' % file_name, file_name)
