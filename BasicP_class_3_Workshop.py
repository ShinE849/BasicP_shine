sword = 20
bow = 10
fist = 5
monster = 100

while True:
    print("สู้ไม่สู้")
    print("1.หนีมัน ไม่สู้ละ")
    print("2.ตีหัวแม่ง")
    kiritoo = int(input("เลือก: "))
    if kiritoo == 1:
        break
    elif kiritoo == 2:
        round = int(input("จะตีกี่ทีใส่เลขไอโง่: "))
        print("มีให้มึงเลือก 3 อย่าง")
        print("sword bow fist: ")
        for i in range(round):
            choice = input()
            if choice == sword:
                monster = sword - monster
            elif choice == bow:
                monster = bow - monster
            elif choice == fist:
                monster = fist - monster
            else:
                print("เริ่มใหม่ไป")
            print("เลือด monster เหลือ: ", monster)
    break        