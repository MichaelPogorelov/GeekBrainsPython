# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('num.txt', 'w') as num_txt:
    num_txt.write(input('Введите числа через пробел:\n'))

with open('num.txt', 'r') as num_txt:
    num_list = num_txt.read().split()

result = 0
for i in num_list:
    result += int(i)
print(result)