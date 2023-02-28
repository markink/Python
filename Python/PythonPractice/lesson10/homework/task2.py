"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


class ByteFormat:
    def value_byte(self, value):
        for s in value:
            print(f'Тип переменной: {format(type(s))}\n'
                  f'Содержание: {format(s)}\n'
                  f'Длина строки: {format(len(s))}')


str_words = [b'class', b'function', b'method']

OBJ = ByteFormat()
OBJ.value_byte(str_words)
