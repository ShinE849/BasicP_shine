# def pnt_hello(year):
#     print("Hello Starter Pack #", year)

# pnt_hello(31)
# pnt_hello(True)
# pnt_hello(3.14)


# def my_sum(num1, num2):
#     return num1 + num2

# sum_riw_vava = my_sum(14, 94)
# print(sum_riw_vava)

# สร้าง function
# จะกินข้าว ต้องมีข้าวก่อน
# จากนั้นต้องมีช้อน ถึงจะกินข้าวได้

# def eat_rice(has_rice, has_spoon):
#     if has_rice == True and has_spoon:
#         return "อยากกินข้าว มีช้อน ได้กินข้าวแล้ว"
#     else:
#         return "ไม่มีข้าว หรือ ไม่มีช้อน อดกินน"
# print(eat_rice(True, False))


# def calculator(num1, num2, cmd):
#     if cmd == "sum":
#         return ("ผลบวกคือ",+num1, +num2)
#     elif cmd == "minus":
#         return ("ผลลบคือ", -num1, -num2)
# print(calculator(5,5,"minus"))
# print(calculator(5,5,"sum"))


# def pnt_n_times(times):
#     for t in range(1, times+1):
#         print(t, "hello world man")
# print(pnt_n_times(4))

# box = ["pen", 30, True,"ruler"]
# print(box[0])
# print(box[3])
# print(box[1])
# box[0] = "book"
# print(box[0])

# box.append("pen")
# print("append", box)

# box.pop(0)
# print("pop", box)


# for i in range(4):
#     print(i, "StarterPack")

# print("---------------------------")

# for i in box:
#     print(i,"box")


# def blox_fruit = ["apple", "orange", "dragon fruit"]
# for fruit in "blox_fruit":
#     if fruit == "apple":
#         print(fruit,"apple kodsab")
#     elif fruit in "blox_fruit":
#         print(fruit, "orange kodsab")
#     else:
#         print(fruit,"ไม่เห็นเจอเลย")
# print()



# blox_fruit = ["apple", "orange", "dragon fruit"]
# def findfruit(name_fruit):
#     for fruit in blox_fruit:
#         if fruit == name_fruit:
#             print("Founded")
#         elif fruit == name_fruit:
#             print("Not Founded")
#         else:
#             print("Not Founded!")
# findfruit("orange")

# students = {"name_student": "Patiwat Pasomsri", "age": 19, "ID": 68130500094}
# print(students)
# print(students["ID"])
# print(students["age"])
# students["age"] = 20
# print(students["age"])
# students["gender"] = "male"
# print(students)

# students = {"name_student": "Patiwat Pasomsri", "age": 19, "ID": 68130500094}

# if students["age"] >= 18:
#     print("ผ่าน เข้าร้านเหล้าได้แล้ว")
# else:
#     print("ไม่ผ่านเว้ย อายุมึงไม่ถึงเข้าไม่ได้ไอสัส")

students = [{"name": "Thanasorn Dusadeeroj", "age": 16, "ID": 67130500014},
            {"name": "satit", "age": 19, "ID": 6713050047}]
for student in students:
    if student["age"] >= 18:
        student["age"] = ("เกินนะ อายุเยอะแล้ว")
    elif student["age"] < 18:
        student["age"] = ("ไม่เกิน อายุน้อยอยู่")
    print(student["age"])