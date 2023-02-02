# Задание 2.
#
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и только арифметические операции.
# Не используйте взятие по индексу.
#
# Пример:
# Ведите целое положительное число: 123456789
# Самая большая цифра в числе: 9

enter_int_value = int(input('Введите целое положительно число'))


def max_number (enter_value):
    max_value = 0
    while enter_value > 0:
        if max_value < enter_value%10:
            max_value = enter_value % 10

        enter_value = enter_value/10

    return round(max_value, 0)


print(max_number(enter_int_value))
