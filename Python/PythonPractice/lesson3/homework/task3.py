# 3. Реализовать структуру «Рейтинг», представляющую собой не
# возрастающий набор натуральных чисел
# (каждый элемент ряда меньше или равен предыдущему).
#
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].


enter_list = input('Введите числа через пробел: ').split()
result_list = list(map(int, enter_list))
enter_value = int(input('Введите число которое необходимо добавить в рейтинг: '))


def sort_number(number_array):
    list.sort(number_array)
    list.reverse(number_array)
    print(number_array)
    return number_array


def add_number(number_array, new_value):
    number_array.append(new_value)
    list.sort(number_array)
    list.reverse(number_array)
    print(number_array)


sort_array = sort_number(result_list)
add_number(sort_array, enter_value)
