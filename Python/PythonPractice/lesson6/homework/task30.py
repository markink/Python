# Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

enter_first_element = int(input('Введите первый элемент массива: '))
enter_difference = int(input('Введите разность: '))
enter_quantity = int(input('Введите количетсво элементов: '))


def fill_array(first_element, difference, quantity):
    index = 1
    filled_array = []
    while quantity >= index:
        filled_array.append(first_element + (index-1)*difference)
        index = index + 1

    return filled_array


print(fill_array(enter_first_element, enter_difference, enter_quantity))
