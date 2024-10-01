# module_3_4.py
# 01.10.2024 Задача "Однокоренные"

def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        m = str(other_words[i].lower()).count(str(root_word.lower()))
        n = str(root_word.lower()).count(str(other_words[i].lower()))
        if m != 0:
            same_words.append(other_words[i])
        if n != 0:
            same_words.append(other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
