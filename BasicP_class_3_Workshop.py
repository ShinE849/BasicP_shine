sword = 50
bow = 30
fist = 10
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
        for i in range(round):
            print("มีให้มึงเลือก 3 อย่าง")
            print("sword bow fist: ")
            choice = input()
            if choice == "sword":
                monster = monster - sword
                print("-50 เลือดมอนเหลือ", monster)
            elif choice == "bow":
                monster = monster - bow
                print("-30 เลือดมอนเหลือ", monster)
            elif choice == "fist":
                monster = monster - fist
                print("-10 เลือดมอนเหลือ", monster)
            else:
                print("เริ่มใหม่ไป")
        if monster == 0:
             break
        else:
            monster = 100
            print("ไปเริ่มใหม่ไป")  