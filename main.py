# module_1_5.py
# 15.09.2024 Неизменяемые и изменяемые объекты. Кортежи и списки
immutable_var=([9], 1, True, "string", 1.5)
print(immutable_var)
immutable_var[0][0]=5
print("Immutable var:", immutable_var)
# immutable_var[1][1]=5
# Изменить неизменные элементы в кортеже нельзя, т.к объект не поддерживает данную функцию.
mutable_list=[1, 2, "a", "b"]
mutable_list[0]="one"
mutable_list[1]="two"
mutable_list[2]="A"
mutable_list[3]="B"
mutable_list.append("Modified")
print("Mutable list:", mutable_list)