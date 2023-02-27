# """Домашнее задание к уроку 7. Задание 2. Рассчиатть массу асфальта"""
# Сделали аттребуты length_road и width_road дескриптерами и проверили их на неотрицательность.


class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, my_value):
        if my_value < 0:
            raise ValueError("Значение не может быть отрицательным")
        instance.__dict__[self.my_attr] = my_value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    # Сделаем атрибуты дескрипторами
    length_road = NonNegative()
    width_road = NonNegative()

    def __init__(self, length_road, width_road):
        self.length_road = length_road
        self.width_road = width_road

    def road_weight(self):
        return self.length_road * self.width_road


OBJ = Road(-110, 20)
# print(OBJ.road_weight())
# OBJ.length_road(-10)
# OBJ.width_road(20)
print(OBJ.road_weight())
