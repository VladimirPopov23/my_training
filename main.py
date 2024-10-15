# module_4_2.py
# 15.10.2024 Домашнее задание по уроку "Пространство имен"

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
# inner_function()
# вызов функции inner_function вне test_function приводит к ошибке, т.к. функция не может быть вызвана за пределами объемлющей области видимости.
