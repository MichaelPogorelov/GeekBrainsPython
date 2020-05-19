# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def some_function(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print('На 0 делить нельзя')

while True:
    number1 = input('Введите первое число:\n')
    number2 = input('Введите второе число:\n')
    if number1.isdigit() and number2.isdigit():
        break
    print('Неправильный ввод')

print(some_function(int(number1), int(number2)))