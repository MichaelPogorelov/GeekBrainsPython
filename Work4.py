# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

while True:
    number = input('Введите целое положительное число\n')
    if number.isdigit():
        max_num = 9
        while str(max_num) not in number:
            max_num -= 1
        print(max_num)
        break
    else:
        print('Некорректное число')