# Создать метакласс для паттерна Синглтон согласно описания в конце лекции №9
# В таком случае результатом (obj_1 is obj_2) будет true

class TypedMeta(type):

    def __init__(self, *args, **kwargs):
        self.a = None

    def __call__(self, *args, **kwargs):
        if self.a == None:
            self.a = super().__call__(*args, **kwargs)
            return self.a
        else:
            return self.a


class MyClass(metaclass=TypedMeta):

    def method1(self):
        pass


obj_1 = MyClass()
obj_2 = MyClass()

print(obj_1 is obj_2)
