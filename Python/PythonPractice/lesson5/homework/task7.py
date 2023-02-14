# Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.
# Пример:
# для n = 5
# 1+2+3+4+5 = 5(5+1)/2
# Нужно написать рекурсивную ф-цию только для левой части выражения!
# Результат нужно сверить с правой частью.
# Правой части выражения в рекурсивной ф-ции быть не должно!
# Решите через рекурсию. В задании нельзя применять циклы.

enter_number = int(input('Введите натуральное число: '))
sum = int(enter_number*(enter_number+1)/2)


def sum_number(number, first_value=1, summ=0):
    if number >= first_value:
        return sum_number(number, first_value+1, summ+first_value)
    else:
        return summ


recursion_sum = int(sum_number(enter_number))
print(f'sum = {sum}, recursion_sum = {recursion_sum}')


if recursion_sum == sum:
    print('Да, выражения равны')
else:
    print('Неверное утверждение 1+2+...+n = n(n+1)/2,')
