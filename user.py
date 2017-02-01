user = input('User: ')
pass_word = input('Password: ')
num = 0
with open('e:/learn_python/user.txt','w') as f:
    f.write(user+pass_word)
