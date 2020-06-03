# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, list_list):
        self.list = list_list

    def __str__(self):
        return '\n'.join([' '.join(map(str, i)) for i in self.list])

    def __add__(self, other):
        new_list = []
        for i in range(len(self.list)):
            new_list.append([self.list[i][j] + other.list[i][j] for j in range(len(self.list[i]))])
        return Matrix(new_list)

new_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(new_matrix)
print(new_matrix + new_matrix1)