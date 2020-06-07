# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return f'{self.num1 + other.num1} + {self.num2 + other.num2}*j'

    def __mul__(self, other):
        return f'{self.num1 * other.num1} + {self.num2 * other.num2}*j'

a = ComplexNumbers(1, 3)
b = ComplexNumbers(2, 4)

print(a + b)
print(a*b)