# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class OfficeEquipmentStore:
    size_of_store = 100
    count = 0
    list_of_units = []

    @classmethod
    def unit_to_store(cls, unit):
        cls.list_of_units.append([unit.name, unit.model, unit.price, unit.count])
        cls.size_of_store -= unit.size * unit.count
        cls.count += unit.count

    @classmethod
    def unit_out_store(cls, unit):
        cls.list_of_units.remove([unit.name, unit.model, unit.price, unit.count])
        cls.size_of_store += unit.size * unit.count
        cls.count -= unit.count


class OfficeEquipment:
    def __init__(self, name, model, price, count):
        self.name = name
        self.model = model
        self.price = price
        try:
            self.count = int(count)
        except ValueError:
            print('Количество должно быть типа int')

class Printer(OfficeEquipment):
    size = 3

class Scaner(OfficeEquipment):
    size = 1

class Copier(OfficeEquipment):
    size = 2


a = Printer('Epson', 'L222', 100, 1)

OfficeEquipmentStore.unit_to_store(a)
OfficeEquipmentStore.unit_out_store(a)

print(OfficeEquipmentStore.list_of_units)