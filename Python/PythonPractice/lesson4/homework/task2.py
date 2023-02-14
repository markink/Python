# Задача №31:
# Напишите программу, которая составит список простых множителей числа N.
# '''

enter_value = int(input("Введите число: "))


def multiplier_number(input_value):
    lst = []
    index = 2
    print(input_value)
    while index <= input_value:
        if input_value % index == 0:
            lst.append(index)
            input_value //= index
            index = 2
        else:
            index += 1
    return lst


find_number = multiplier_number(enter_value)
print(f"Простые множители числа {enter_value} \n {find_number}")
