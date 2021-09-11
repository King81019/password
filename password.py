chance = 3
while True:
    pw = input('請輸入密碼：')
    if pw == 'a123456':
        print('成功登入')
        break
    elif chance > 1:
        chance = chance - 1
        print('你還有', chance, '次機會')
    else:
        print('錯誤三次 帳號鎖定')
        break


