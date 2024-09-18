# module_2_2.py
# 18.09.2024 Условная конструкция. Операторы if, elif, else.
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)