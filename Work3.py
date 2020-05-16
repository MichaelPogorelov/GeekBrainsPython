# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

some_list = ['зима', 'весна', 'лето', 'осень']
while True:
    month = input('Введите месяц от 1 до 12:\n')
    if month.isdigit() and 0 < int(month) < 13:
        break
    print('Неправильное число')
month = int(month)
if 2 < month < 6:
    print(some_list[1])
elif 5 < month < 9:
    print(some_list[2])
elif 8 < month < 12:
    print(some_list[3])
else:
    print(some_list[0])
some_dict = {
    1:'зима',
    2:'зима',
    3:'весна',
    4:'весна',
    5:'весна',
    6:'лето',
    7:'лето',
    8:'лето',
    9:'осень',
    10:'осень',
    11:'осень',
    12:'зима'
}
print(some_dict[month])


