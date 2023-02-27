# """Домашнее задание к уроку 7. Задание 3. Реализовать класс базовый класс Worker и класс Postion"""
# Сделали аттребуты wage и bonus дескриптерами и проверили их на неотрицательность.

class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, my_value):
        if my_value < 0:
            raise ValueError("Значение не может быть отрицательным")
        instance.__dict__[self.my_attr] = my_value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    # "Дескрипторы"
    wage = NonNegative()
    bonus = NonNegative()

    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position

        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        # print(f'Сотрудника зовут {self.name} {self.surname}')
        return self.name + ' ' + self.surname

    def get_total_income(self):
        # print(f'Зарплата сотрудника {sum(self._income.values())}')
        return sum(self._income.values())


OBJ1 = Position('Ivan', 'Ivanov', 'Engineer', 400, 20)
print(f'Зарплата сотрудника {OBJ1.get_total_income()}')
OBJ1.wage = -19
print(f'Зарплата сотрудника {OBJ1.get_total_income()}')
