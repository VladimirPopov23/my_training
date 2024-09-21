# module_2_3.py
# 21.09.2024 Нули ничто, отрицание недопустимо!
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
my_list.remove(0)
while a < len(my_list):
    if my_list[a] < 0:
        break
    print(my_list[a])
    a = a + 1