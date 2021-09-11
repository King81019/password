chance = 3
password = 'a123456'
while True:
    pw = input('請輸入密碼：')
    if pw == password:
        print('成功登入')
        break
    else:
        chance = chance - 1
        if chance == 0:
            print('錯誤三次 帳號鎖定')
            break
        else:
            print('密碼錯誤！ 你還有', chance, '次機會')


