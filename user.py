user_dict = {'John': '11111'}  # 用户名 密码
num = 0                        # 重试次数


with open('/learn_python/learn_python/user.txt', 'r') as f_r:   #读取用户重试次数
    error_num = int(f_r.read())
# 循环输入
while num < 3:
    user = input('User: ')
    pass_word = input('Password: ')
    if (error_num == 3):    # 如果用户之前已经超过次数直接退出
        print('超过次数')
        break
    else:
        if (pass_word == user_dict['John']):    #判断密码是否正确
            print('成功登陆')
            break
        else:
            print('密码错误')
            num += 1
    with open('/learn_python/learn_python/user.txt', 'w') as f:  #写入用户的重试次数
        f.write(str(num))
