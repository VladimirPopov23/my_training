# module_3_2.py
# 29.09.2024 Задача "Рассылка писем" (устранение замечаний)

def send_email(message, recipient, *, sender="university.help@gmail.com"):
    x = (".com", ".ru", ".net")
    index_r = recipient.find("@")
    index_s = sender.find("@")
    if int(index_r) > 0 and int(index_s) > 0:
        index = True
    else:
        index = False
    for n in recipient and sender:
        if recipient.endswith(x) and sender.endswith(x):
            n = True
        else:
            n = False
    if sender == "university.help@gmail.com" and index == True and n == True:
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    if sender != "university.help@gmail.com" and recipient != sender and index == True and n == True:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
    if index == False or n == False:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
