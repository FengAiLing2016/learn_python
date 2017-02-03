#!/usr/bin/env python
#_*_coding:utf-8_*_
num = 1
temp = 1
# 判断用户名是否被锁定
while num:
    user = input('User: ')  # 输入用户名
    f = open('/learn_python/learn_python/user/user_lock.txt', 'r')  # 打开锁定用户列表
    # 判断
    for line in f.readlines():
        if user == line.strip('\n'):
            print('lock!')
            num = 0
            break
        else:
            num = 0
            temp = 2
    f.close()
# 判断密码输入是否正确
if temp == 2:
    f = open('/learn_python/learn_python/user/user.txt', 'r')  # 打开用户列表
    for line in f.readlines():
        user_save, pass_save = line.strip('\n').split()
        if user == user_save:  # 判断用户名
            while num < 3:  # 重试3次
                pass_word = input('Password: ')  # 输入密码
                if pass_word == pass_save:  # 判断密码正确
                    print('good!')
                    num = 5
                else:
                    print('password is error')  # 提示密码错误
                    num += 1  # 重试次数
            break  # 如果用户名正确跳出循环不再进行剩余的用户名判断
    f.close()
# 当重试次数=3次将用户名写入锁定列表
    if num == 3:
        with open('/learn_python/learn_python/user/user_lock.txt', 'a') as f:
            f.write('\n' + user)
