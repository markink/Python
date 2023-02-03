# Задание 1.

# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня,
# на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.
#
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

enter_current_distance = int(input('Введите расстояние для первого дня'))
enter_target_distance = int(input('Введите цель, которую хотите достигнуть'))


def days_totarget(first_distance, final_distance):
    index = 1
    while first_distance < final_distance:
        first_distance = first_distance + first_distance / 10
        print(f'{index}-й день: {round(first_distance, 2)}')
        index = index + 1
    print(f'На {index-1}-й день спортсмен достиг результата - не менее {final_distance} км')


days_totarget(enter_current_distance, enter_target_distance)
