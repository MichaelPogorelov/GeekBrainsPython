# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

some_list = []
i = 0
while True:
    element = input('Введите элемент(если хотите пропустить введите "break"):\n')
    if element == 'break':
        break
    some_list.append(element)
if len(some_list)%2 == 0:
    while i < len(some_list):
        some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
        i += 2
else:
    while i < len(some_list) - 1:
        some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
        i += 2
print(some_list)

