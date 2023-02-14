# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.
from random import random

generate_number = int(round(random()*100, 0))
print(generate_number)


def guess_number (number, index=0):
    if index < 10:
        print(f"Количество попыток: {index}")
        enter_number = int(input('Введите загаданное число: '))
        if enter_number == number:
            print(f'Вы угадали это число {number}')
        else:
            return guess_number(number, index+1)
    else:
        print(f'Ваши попытки закончились :(\nЗагаданное число {number}')


guess_number(generate_number)
