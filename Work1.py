# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
from itertools import cycle

class TrafficLight:
    __color = {'красный': 7, 'желтый': 2, 'зеленый': 7}
    def running(self, count):
        count *= 3
        for color, time in cycle(TrafficLight.__color.items()):
            if not count:
                break
            print(color)
            sleep(time)
            count -= 1

new_traffic_light = TrafficLight()
new_traffic_light.running(1)