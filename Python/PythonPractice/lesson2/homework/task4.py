# Задание 4. Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
#
# Пример:
# Введите целые числа через пробел: 1 2 3 4
# Результат: 2 1 4 3
#
# Введите целые числа через пробел: 1 2 3
# Результат: 2 1 3

el_count = input("Введитe целые числа через пробел ").split()


def exchange_elements (input_elements):
    i = 0
    print(f'Массив до обработки: {input_elements}')
    for elem in range(int(len(input_elements)/2)):
        input_elements[i], input_elements[i + 1] = input_elements[i+1], input_elements[i]
        i += 2

    print(f'Результат обработки: {input_elements}')


exchange_elements(el_count)


