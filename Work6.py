# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


#Пример текстового файла:
# Алгебра: 50(л) 50(пр) 50(лаб)
# Химия: 50(пр) 30(лаб)
# Информатика: 100(л) 50(пр) 20(лаб)
# Физика: 30(л) 10(лаб)
# Физкультура: 30(пр)

# Создаем словарь
lesson_dict = {}

with open('text.txt', 'r') as text:
    for line in text:
        # получаем строчку от первой цифры до конца строки, удаляя л, пр и лаб и создаем из нее список
        val = line[line.find(':') + 1:].replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').split()
        # записываем в словарь ключ - название предмета и значение - количество занятий
        lesson_dict[line[:line.find(':')]] = sum(int(i) for i in val)

print(lesson_dict)