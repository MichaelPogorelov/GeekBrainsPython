# 6. Реализовать функцию int_func(),
# принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

# С функцией title
# def int_func(text):
#     return text.title()

# Без функции title
def int_func(text):
    First_Letter = chr(ord(text[0]) - 32)
    next_letter = text[1:]
    return First_Letter + next_letter

some_text = 'this is the example'
text_list = some_text.split()
Text_List = []
for i in text_list:
    Text_List.append(int_func(i))
print(' '.join(Text_List))