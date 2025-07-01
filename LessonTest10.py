# ДЗ 13.1
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} y.o., {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record book: {self.record_book}"

    # Щоб можна було додати у set
    def __eq__(self, other):
        return isinstance(other, Student) and self.record_book == other.record_book

    def __hash__(self):
        return hash(self.record_book)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(s) for s in self.group)
        return f"Group Number: {self.number}\n{all_students}"


#ДЗ 13.2
# class Counter:
#
#     def __init__(self, current=1, min_value=0, max_value=10):
#         self.current = current
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def set_current(self, start):
#         self.current = start
#
#     def set_max(self, max_max):
#         self.max_value = max_max
#
#     def set_min(self, min_min):
#         self.min_value = min_min
#
#     def step_up(self):
#         if self.current < self.max_value:
#             self.current += 1
#         else:
#             raise ValueError("Досягнуто максимуму")
#
#     def step_down(self):
#         if self.current > self.min_value:
#             self.current -= 1
#         else:
#             raise ValueError("Досягнуто мінімуму")
#
#     def get_current(self):
#         return self.current