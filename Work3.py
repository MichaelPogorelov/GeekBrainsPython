# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# Создаем файл куда записываем фамилию и оклад
with open('text.txt', 'w' ) as text:
    while True:
        a = input('Фамилия, оклад: ')
        if a == '':
            break
        text.writelines(a + '\n')

# Читаем из файла данные и заносим их в словарь
with open('text.txt', 'r') as text:
    person_dict = {}
    for num, person in enumerate(text, 1):
        person_dict[person[:person.find(',')]] = int(person[person.rfind(' ') + 1 : -1 if '\n' in person else None])

# Выводим фамилии сотрудников у которых оклад меньше 20000
for key, val in person_dict.items():
    if val < 20000:
        print(key)

# Выводим среднюю величину дохода
print(f'Средняя величина дохода - {sum(person_dict.values())/num}')