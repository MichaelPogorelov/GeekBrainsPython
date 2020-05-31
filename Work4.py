# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        if self.direction == 'left':
            print('Поворот на лево')
        elif self.direction == 'right':
            print('Поворот на право')
        else:
            print('Неверная команда')

    def show_speed(self):
        print(f'Скорость {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, model):
        super().__init__(speed, color, name, is_police)
        self.model = model
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police, model):
        super().__init__(speed, color, name, is_police)
        self.model = model

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, model):
        super().__init__(speed, color, name, is_police)
        self.model = model
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, type):
        super().__init__(speed, color, name, is_police)
        self.type = type

town_car_1 = TownCar(65, 'Blue', 'Mazda', False, 6)
town_car_1.show_speed()

sport_car_1 = SportCar(200, 'Red', 'Ferrari', False, '488 Spider')
sport_car_1.turn('left')

work_car_1 = WorkCar(39, 'Orange', 'CAT', False, 'excavator')
print(work_car_1.model)

police_car_1 = PoliceCar(190, 'White', '02', True, 'Test')
print(police_car_1.is_police)