DT = int(input("กรอกระยะทางKMที่ท่านต้องการคำนวณ: "))
if DT <= 4:
    print("ไม่รับคับน้อง")
elif DT <= 50:
    print("ค่าขนส่ง 10 บาท")
elif DT <= 100:
    print("ค่าขนส่ง 15 บาท")
elif DT <= 300:
    print("ค่าขนส่ง 25 บาท")
elif DT <= 500:
    print("ค่าขนส่ง 35 บาท")
else:
    print("ค่าขนส่ง 45 บาท")