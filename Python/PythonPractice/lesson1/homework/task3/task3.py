# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
#
# Пример:
# Введите число n: 3
# n + nn + nnn = 369
enter_value = int(input('Введите целое положительное число'))
output_value = enter_value + enter_value*enter_value + enter_value*enter_value*enter_value
print(f'Результат согласно задания: {output_value}')
output_value = str(enter_value) + str(enter_value*2) + str(enter_value*3)
print(f'Результат согласно вывода в примере: {output_value}')
