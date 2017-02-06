#!/usr/bin/env python
#_*_coding:utf-8_*_
# 查找列表中数据的下标
name = [1, 3, 2, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7,
        6, 5, 4, 3, 3, 1, 2, 3, 5, 6, 2, 4, 7, 1, 3]
first_pos = 0  # 初始下标
for i in range(name.count(2)):  # 统计列表数据的个数
    new_list = name[first_pos:]  # 切片，赋值新的列表
    next_pos = new_list.index(2) + 1  # 将找到的下标值+1赋予下个循环的下标
    print('find postion:', new_list.index(2) + first_pos)  # 打印下标值（加上个循环找到的下标值）
    first_pos += next_pos  # 下标值累加

# index方法 index可以设置范围检索
first_pos = -1  #第一次要从0开始检索所以first_pos初始化为-1
for i in range(name.count(2)):
    first_pos = name.index(2, first_pos + 1)    #从first_pos+1开始检索
    print('Find Postion', first_pos)
