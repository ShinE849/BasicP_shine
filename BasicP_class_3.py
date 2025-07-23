# has_rice = True
# has_spoon = True

# if has_rice:
#     print("มีข้าวแล้ว")
#     if has_spoon:
#         print("มีข้าว กินข้าวได้")
#     else:
#         print("ไม่มีช้อน กินข้าวไม่ได้")
# else:
#     print("ไม่มีข้าว กินไม่ได้")

# ตื่นก่อน
# จากนั้นค่อยเดินทางมามอ
# Wake_up = True
# want_to_go_uni = True
# go_with_motorcycle = True
# if Wake_up:
#     print("ตื่นแล้ว")
#     if want_to_go_uni:
#         print("ตื่นแล้ว ไปมอดีกว่า")
#         if go_with_motorcycle:
#             print("ตื่นละ อยากไปมอด้วยมอไซ")
#         else:
#             print("ตื่นละ อยากไป แต่ไม่อยากขี่มอไซไป ไม่ไปดีกว่า")
#     else:
#         print("ตื่นละ แต่ไม่อยากไปอะ ไม่ไปดีกว่า")
# else:
#     print("ไม่ตื่น")

# for index in range(1, 5+1):
#     print("round", index, "Hello World")

# b = True
# for index in range(1,6+1):
#     if index == 3:
#         print("round", index, "StarterPack")
#         if index == 3:
#             print("round 3",b)
#         else:
#             print("ไม่จริง")
#     else:
#         print("round", index, "Hello world

# ถามผู้ใช้ อยากลบกี่รอบ
# ถามด้วยอยากลขด้วยเลขอะไร
# แล้วนำเลขจากผู้ใช้มาลบ ด้วย เลขที่ถาม
# num = int(input("กรอกเลข: "))
# times = int(input("จำนวนครั้งที่ต้องการ: "))

# for i in range(times):

#     minus_num = int(input())
#     num = num - minus_num
#     print(("เหลือเลข: "), num)


# i = 0
# while i < 5:
#     print("Hello man")
#     # i = i + 1
#     print(i)
#     break

#ถ้าเลือก 1 จะให้เเลือกใหม่
#ถ้าเลือก 2 จะให้จบการทำงาน

while True:
    option = input("Enter number: ")
    if option == "1":
        print("เลือกใหม่")
    elif option == "2":
        break