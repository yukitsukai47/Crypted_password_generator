import os
import secrets
import subprocess

def passmake():

    print('What s site?')
    site = input()
    print('input your username')
    username = input()
    print('How many digits of password do you want to create?')
    digit = int(input())

    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    lchar_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    uchar_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    symbol_list = ['！', '”', '＃', '＄', '％', '＆', '’', '（', '）',
        '＊', '＋', '，', '－', '．', '／', '：', '；', '＜',
        '＝', '＞', '？', '＠', '［', '￥', '］', '＾', '＿',
        '‘', '｛', '｜', '｝', '￣']

    print('Whats option?')
    print('1.Only Number!')
    print('2.Number & Lower case letter!')
    print('3.Number & Lower case letter & uppercase letter!')
    print('4.Number & Lower case letter & uppercase letter & Symbol!')


    x = int(input())
    create_pass_list = []
    if x == 1:
        for _ in range(digit):
            create_pass_list.append(secrets.choice(num_list))

    elif x == 2:
        for _ in range(digit):
            create_pass_list.append(secrets.choice(num_list + lchar_list))

    elif x == 3:
        for _ in range(digit):
            create_pass_list.append(secrets.choice(num_list + lchar_list + uchar_list))

    elif x == 4:
        for _ in range(digit):
            create_pass_list.append(secrets.choice(num_list + lchar_list + uchar_list + symbol_list))
    else:
        print('error')

    print('Created successfully.')
    create_pass = ''
    for x in create_pass_list:
        create_pass += x
    print(create_pass)

    f = open(site + ".txt", 'w')
    password = "WebSite:" + site + "\n" + "UserName:" + username + "\n" + "Password:" + create_pass + "\n"
    f.write(password)
    f.close()

    cmd = 'cat ' + site + ".txt" + '| python3 crypto.py -e > crypted_' + site + '.txt'
    process = (subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0]).decode('utf-8')
    
    print("パスワードファイルの暗号化に成功しました")

    
if __name__ == '__main__':
    passmake()
