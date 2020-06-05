# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def my_error(self):
        try:
            return self.num1/self.num2
        except ZeroDivisionError:
            print('на ноль делить нельзя!')

a = MyError(1, 0)
a.my_error()