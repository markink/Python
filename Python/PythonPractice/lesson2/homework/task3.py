# Задание 3. Создать список и заполнить его элементами различных типов данных.
# Реализовать проверку типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
#
# Пример:
# для списка [5, "string", 0.15, True, None]
# результат
#
# <class 'int'>
# <class 'str'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>

basic_list = [5, 'string', 0.15, True, None]

def output_type_elemnts (basic_list):
    for el in basic_list:
        print(type(el))


output_type_elemnts(basic_list)
