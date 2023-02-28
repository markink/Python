"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

str_list = ['разработка', 'администрирование', 'protocol', 'standard']
for el in str_list:
    encode_el = el.encode('utf-8')
    print(encode_el, type(encode_el))
    decode_el = bytes.decode(encode_el, 'utf-8')
    print(f'{decode_el, type(decode_el)} \n')
