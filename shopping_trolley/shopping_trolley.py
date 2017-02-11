commodity = {
    'Apple iphone': 5800,
    'Book': 55,
    'Vivo xplay6': 4500,
    'Dvd': 300,
    'Computer': 3000}  # 商品字典
select_dict = {}  # 用户选择的商品字典
select_list = []  # 用户选择的商品列表

money = int(input('输入你的金钱：'))
while money > 55:  # 金额必须大雨55，商品的最低金额
    print('''
选择你需要的商品           你的金额：%d
=============================================================================''' % money)
    for i in commodity:
        print('%s:%d' % (i, commodity[i]))  # 格式化操作符的右操作数是字典的话必须将它用圆括号括起来，疑问
    print('''
=============================================================================''')

    com_select = input('输入你要的商品：')
    while com_select in commodity:  # 判断输入的商品是否是商品字典里的商品
        if money >= commodity[com_select]:  # 判断金额是否大于商品金额
            money = money - commodity[com_select]     #减去已选商品金额
            select_dict[com_select] = commodity[com_select]     #将商品字典赋值与用户选择字典
            select_list.append(com_select)      #将已选商品加入列表
            break
        elif money < commodity[com_select]:
            print('超出金额')
            break
    else:
        print('没有此商品，请重新输入')
else:
    print('''剩余金额%s，你的购物车商品如下:
=============================================================================
名称          金额          数量''' % money)
    for temp in select_dict:
        print('%s          %d          %d' %
              (temp, select_dict[temp], select_list.count(temp)))
print('''
=============================================================================''')
