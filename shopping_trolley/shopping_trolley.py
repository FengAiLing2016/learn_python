commodity = {
    'Apple iphone': 5800,
    'Book': 55,
    'Vivo xplay6': 4500,
    'Dvd': 300,
    'Computer': 3000}
select_list={}
money = int(input('输入你的金钱：'))
while money > 55:
    print('''
选择你需要的商品           你的金额：%d
=============================================================================
    ''' % money)
    for i in commodity:
        print('%s:%d' % (i, commodity[i]))  # 格式化操作符的右操作数是字典的话必须将它用圆括号括起来，疑问
    print('''
=============================================================================
    ''')

    com_select = input('输入你要的商品：')
    while com_select in commodity:
        if money >= commodity[com_select]:
            money =money -commodity[com_select]
            select_list[com_select]=commodity[com_select]
            break
        elif money < commodity[com_select]:
            print('超出金额')
            break
    else:print('没有此商品，请重新输入')
else:
    print('剩余金额%s，你的购物车商品如下：' % money)
    for i in select_list:
        print('%s %s' %( i,select_list[i]))
