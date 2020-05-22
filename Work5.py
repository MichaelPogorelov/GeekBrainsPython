# 5. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

for i in count(3):
    if i == 10:
        break
    print(i)

some_list = [1, 2, '3', True, ['a', '6'], {7, False}, 9]
new_some_list = []
for i in cycle(some_list):
    new_some_list.append(i)
    if len(new_some_list) > len(some_list)*5:
        break
