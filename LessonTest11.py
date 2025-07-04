# ДЗ 14.1
# Користувацький виняток
class GroupLimitError(Exception):
    pass

# Базовий клас Людина
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, {self.gender}"

# Клас Студент
class Student:
    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, Залікова: {self.record_book}"

# Клас Група
class Group:
    def __init__(self, number):
        self.number = number
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupLimitError("У групі вже 10 студентів!")
        self.students.append(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)

    def __str__(self):
        text = f"Група: {self.number}\n"
        for s in self.students:
            text += str(s) + '\n'
        return text.strip()


# ДЗ 15.1

# import math
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         return self.get_square() == other.get_square()
#
#     def __add__(self, other):
#         total_area = self.get_square() + other.get_square()
#         side = math.sqrt(total_area)
#         return Rectangle(round(side), math.ceil(total_area / round(side)))
#
#     def __mul__(self, n):
#         new_area = self.get_square() * n
#         side = math.sqrt(new_area)
#         return Rectangle(round(side), math.ceil(new_area / round(side)))
#
#     def __str__(self):
#         return f"Прямокутник {self.width}x{self.height}, площа: {self.get_square()}"


#  ДЗ 15.2

# class Fraction:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __mul__(self, other):
#         num = self.a * other.a
#         den = self.b * other.b
#         return Fraction(num, den)
#
#     def __add__(self, other):
#         num = self.a * other.b + other.a * self.b
#         den = self.b * other.b
#         return Fraction(num, den)
#
#     def __sub__(self, other):
#         num = self.a * other.b - other.a * self.b
#         den = self.b * other.b
#         return Fraction(num, den)
#
#     def __eq__(self, other):
#         return self.a * other.b == other.a * self.b
#
#     def __gt__(self, other):
#         return self.a * other.b > other.a * self.b
#
#     def __lt__(self, other):
#         return self.a * other.b < other.a * self.b
#
#     def __str__(self):
#         return f"Fraction: {self.a}, {self.b}"
