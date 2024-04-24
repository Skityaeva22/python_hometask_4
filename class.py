# задание 1 (прямоугольник)
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_info(self):
        print(f'Сторона A = {self.a}, сторона B = {self.b}')

    def get_perimeter(self):
        self.perimeter = 2 * (self.a + self.b)
        print(f'Периметр = {self.perimeter}')

    def get_square(self):
        self.square = self.a * self.b
        print(f'Площадь = {self.square}')

print('задание 1')
r = Rectangle(10, 12)
r.get_info()
r.get_perimeter()
r.get_square()
print('')

# задание 2
from datetime import date

todays_date = date.today()

class Human:
    def __init__(self, name, city, birth_year):
        self.name = name
        self.city = city
        self.birth_year = birth_year

    def get_age(self):
        self.age = todays_date.year - self.birth_year
        print(f'Возраст {self.name}, проживающего в г. {self.city} составляет {self.age} года')

print('задание 2')
h = Human('Вася', 'Уфа', 2000)
h.get_age()
print('')

# задание 3
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_info(self):
        print(f'x = {self.x}, y = {self.y}')

    def addition_operation(self):
        self.addition = self.x + self.y
        print(f'x + y = {self.addition}')

    def subtraction_operation(self):
        self.subtraction = self.x - self.y
        print(f'x - y = {self.subtraction}')

    def multiplication_operation(self):
        self.multiplication = self.x * self.y
        print(f'x * y = {self.multiplication}')

    def exponentiation_operation(self):
        self.exponentiation = self.x ** self.y
        print(f'x в степени y = {self.exponentiation}')

    def division_operation(self):
        if self.y != 0:
            self.division = self.x / self.y
            print(f'x поделить на y = {self.division}')
        else:
            print(f'При делении на 0 получаете +/- бесконечность')

    def integer_division_operation(self):
        if self.y != 0:
            self.integer_division = self.x // self.y
            print(f'Целочисленное деление x на y = {self.integer_division}')
        else:
            print(f'При делении на 0 получаете +/- бесконечность')

    def division_remainder_operation(self):
        if self.y != 0:
            self.division_remainder = self.x % self.y
            print(f'Остаток от деления x на y = {self.division_remainder}')
        else:
            print(f'При делении на 0 получаете +/- бесконечность')

print('задание 3')
c = Calculator(5, 13)
c.get_info()
c.addition_operation()
c.subtraction_operation()
c.multiplication_operation()
c.exponentiation_operation()
c.division_operation()
c.integer_division_operation()
c.division_remainder_operation()
print('')

# задание 4
class Student:
    def __init__(self, name, age, univercity, city, course):
        self.name = name
        self.age = age
        self.univercity = univercity
        self.city = city
        self.course = course

    def __str__(self):
        return f'Студент {self.name} из г.{self.city} в возрасте {self.age} обучается в {self.univercity} на {self.course} курсе'

print('задание 4')
s = Student('Вася Пупкин', 'Салават', 'УУНиТ', 20, 3)
print(str(s))
print('')

# задание 5
from random import randint

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_salary(self):
        salary = randint(20000, 50000)
        return salary

    def __str__(self):
        return f'{self.position} {self.name} получает з/п в размере {self.get_salary()} руб.'

class Manager(Employee):
    pass

class Worker(Employee):
    pass

manager = Manager("Вася Пупкин", "Менеджер")
worker = Worker("Петр Васин", "Работник")

print('задание 5')
print(str(manager))
print(str(worker))
print('')
