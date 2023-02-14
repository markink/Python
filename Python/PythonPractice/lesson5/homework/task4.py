# Задание 4. Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
# Пример:
# Введите количество элементов: 3
# Количество элементов - 3, их сумма - 0.75
# Решите через рекурсию. В задании нельзя применять циклы.
# Нужно обойтисть без создания массива!

enter_value = int(input('Ввидите количество элементов: '))
start_value = 1


def summ_elem(input_value, first_value, summ=1):

    if input_value > 1:
        first_value = first_value / -2
        summ = summ + first_value
        return summ_elem(input_value-1, first_value, summ)

    return summ


print(summ_elem(enter_value, start_value))
