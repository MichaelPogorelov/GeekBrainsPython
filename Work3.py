# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    my_list = [num1, num2, num3]
    return sum(my_list) - min(my_list)
print(my_func(1, 2, 3))
