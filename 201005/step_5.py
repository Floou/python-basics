class Door:
    def __init__(self):
        self.height = None
        self.width = None
        self.material = None


class Car:
    def __init__(self):
        self.engine = None
        self.color = None
        self.brand = None
        self.mark = None


class MyAdminUser:
    def __init__(self):
        self.name = None
        self.age = None
        self.level = 0


user_1 = MyAdminUser()
# print(type(user_1))
# print(dir(user_1))
user_1.name = 'Иван'
user_1.age = 18
user_1.level = 2
print(user_1, user_1.name, user_1.age)

user_1.age = 19
print(user_1, user_1.name, user_1.age)

user_2 = MyAdminUser()
user_2.name = 'Петр'
print(user_2, user_2.name, user_2.age)