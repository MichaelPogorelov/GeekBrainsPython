# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

#функция возвращает сумму чисел
def my_func(*args):
    some_list = []
    for i in args:
        some_list.append(int(i))
    return sum(some_list)

#переменная для выхода из цикла
bool_var = False
#переменная куда будет сохраняться результат
result = 0

while True:
    numbers = input('Введите числа через пробел или @ для завершения программы:\n')
    if '@' in numbers:
        bool_var = True
        numbers1 = numbers.replace('@', '').replace(' ', '')
        if numbers1.isdigit():
            result += my_func(*numbers.replace('@', '').split())
        else:
            print('Неправильный ввод')
    else:
        numbers1 = numbers.replace(' ', '')
        if numbers1.isdigit():
            result += my_func(*numbers.split())
        else:
            print('Неправильный ввод')
    print(result)
    if bool_var:
        break

