#Задача №30:
# Вычислить число c заданной точностью d.
# Пример:


from math import pi

d = int(input("Введите число знаков после запятой: "))
print(f'число Пи и {d} знаков после запятой {round(pi, d)}')
