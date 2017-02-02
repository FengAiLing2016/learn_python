num = 0
temp = 1
# 循环输入
while num < 3:
    user = input('User: ')
    f = open('/learn_python/learn_python/learn_python/user/user_lock.txt', 'r')
    for line in f.readlines():
        if user == line:
            print('lock!')
            temp = 0
            num=4
            break
    f.close()
    if temp:
        f = open('/learn_python/learn_python/learn_python/user/user.txt', 'r')
        for line in f.readlines():
            pass_word = input('Password: ')
            user_save, pass_save = line.strip('\n').split()
            if user == user_save:
                if pass_word == pass_save:
                    print('good!')
                    num = 6
                    break
                else:
                    num += 1
            elif user != user_save:
                print('not user')
        f.close()
if num == 3:
    with open('/learn_python/learn_python/learn_python/user/user_lock.txt', 'a') as f:
        f.write(user)
