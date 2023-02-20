# Задание 1.
#
# Создать класс TrafficLight (светофор)
# и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
#
# В рамках метода running реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
# Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
#
# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
#
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
from time import sleep


class TrafficLight:
    _color = ['Красный', 'Желтый', 'Зелёный']

    @staticmethod
    def running():
        colors = TrafficLight._color
        green_delay = 7
        yellow_delay = 2
        red_delay = 5
        print(colors[0])
        sleep(green_delay)
        print(colors[1])
        sleep(yellow_delay)
        print(colors[2])
        sleep(red_delay)
        return TrafficLight.running()


TrafficLight.running()
