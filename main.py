# module_3_1.py
# 26.09.2024 Задача "Счётчик вызовов"

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(line):
    argument = str(line)
    result = (len(argument), argument.upper(), argument.lower())
    count_calls()
    return result


def is_contains(line, list_):
    line = str(line).lower()
    count_calls()
    for i in range(len(list_)):
        if str(list_[i]).lower() == line:
            result = True
            break
        else:
            result = False
            continue
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)