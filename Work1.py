# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_int(cls, date):
        day = int(date[:date.find('-')])
        month = int(date[date.find('-') + 1:date.rfind('-')])
        year = int(date[date.rfind('-') + 1:])
        return day, month, year

    @staticmethod
    def valid(day, month, year):
        if month in (1, 3, 5, 7, 8, 10, 12):
            return True if 0 < day < 32 else False
        elif month in (4, 6, 9, 11):
            return True if 0 < day < 31 else False
        elif month == 2:
            if year%4 != 0:
                return True if 0 < day < 29 else False
            elif year%100 == 0 and year%400 != 0:
                return True if 0 < day < 29 else False
            else:
                return True if 0 < day < 30 else False
        else:
            return False





a = Date('21-03-2013')
print(a.date_int('21-03-2013'))
print(Date.valid(*a.date_int('21-03-2013')))