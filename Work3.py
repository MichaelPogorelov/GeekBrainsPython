# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

while True:
    number = input('Введите число\n')
    if number.isdigit():
        print(int(number) + int(number * 2) + int(number * 3))
        break
    else:
        print('Некорректное число')