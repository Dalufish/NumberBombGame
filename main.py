import random as rd
#數字炸彈基礎版:)
def nbo1():
    rdnum = rd.randint(1,11)
    print("歡迎遊玩\"數字炸彈\":)")
    usernum = int(input("請猜猜一個1~10之間的整數:"))
    if rdnum == usernum:
        print("系統數字為",rdnum,"您輸入的是",usernum,"數字匹配,恭喜獲勝")
    else:
        print("系統數字為",rdnum,"您輸入的是",usernum,"數字不匹配,失敗")
# 數字炸彈進階版:D
def nbo2():
    truenumber = str(rd.randint(1,11))
    print("歡迎遊進階版\"數字炸彈\":D")
    while True:
        guessnumber = input("請猜猜一個1~10之間的整數:")
        if guessnumber == truenumber:
            print("恭喜猜對了!")
            break
        else:
            print("猜錯了,再試試看吧")
    print("感謝遊玩.w.")
# 數字炸彈究極版XD
def nbo3():
    rdnum = str(rd.randint(1,11))
    print("歡迎遊究極版\"數字炸彈\"XD")
    for x in range(3):
        if x == 0:
            guessnumber = input("請猜猜一個1~10之間的整數,只有3次機會喔:")
            if guessnumber == rdnum:
                print("太厲害了,第一次就猜對!")
                break
        if x == 1:
            guessnumber = input("剩2次機會了喔:")
            if guessnumber == rdnum:
                print("恭喜猜對了!")
                break
        if x == 2:
            guessnumber = input("剩下最後1次機會...:")
            if guessnumber == rdnum:
                print("恭喜答對了!")
                break
            else:
                print("用完所有機會了,失敗:(")
    print("感謝遊玩~")

    
