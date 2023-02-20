# Задание 5.
# 1) Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
# работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.


class DivisionByNull:
    def __init__(self, dividend, divider):
        self.dividend = int(dividend)
        self.divider = int(divider)

    @staticmethod
    def divide_by_null(dividend, divider):

        if divider == 'stop':
            print("Счастливого дня")
            return

        try:
            divider = int(divider)
            dividend = int(dividend)
        except:
            print('Введён недопустимый тип для числа')
            return DivisionByNull.divide_by_null(input('Введите делимое: '), input('Введите делитель("stop" для завершения): '))

        try:
            dividend/divider
        except:
            print('Деление на ноль недопустимо')
            return DivisionByNull.divide_by_null(input('Введите делимое: '), input('Введите делитель("stop" для завершения): '))

        print(f'результатом деления {dividend} на {divider} равно {dividend / divider}')
        return DivisionByNull.divide_by_null(input('Введите делимое: '), input('Введите делитель("stop" для завершения): '))


DivisionByNull.divide_by_null(100, 0)