"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


str_word1 = b'attribute'
str_word2 = b'класс'
str_word3 = b'функция'
str_word4 = b'type'
#
# Слова с руссикими буквами невозможно преобразовать через b''
# str_word2 = b'класс'
#                              ^
# SyntaxError: bytes can only contain ASCII literal characters

