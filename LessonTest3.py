# ДЗ 5.1. Ім'я змінної

import string
import keyword

name = input("Введіть ім'я змінної: ")
if name == "_":
    print(True)
elif set(name) == {"_"}:
    print(False)

else:
    дозволено = True
    if name[0].isdigit():
        дозволено = False

    for літера in name:
        if літера.isupper():
            дозволено = False

    for знак in string.punctuation:
        if знак != "_" and знак in name:
            дозволено = False

    if name in keyword.kwlist:
        дозволено = False

    print(дозволено)


# ДЗ 5.2. Модифікувати калькулятор
# while True:
#     a = float(input("Введи перше число: "))
#     b = float(input("Введи друге число: "))
#
#     operation = input("Введи операцію (+, -, *, /): ")
#     if operation == "+":
#         print("Результат:", a + b)
#     elif operation == "-":
#         print("Результат:", a - b)
#     elif operation == "*":
#         print("Результат:", a * b)
#     elif operation == "/":
#         if b == 0:
#             print("На нуль ділити не можна!")
#         else:
#             print("Результат:", a / b)
#     else:
#         print("Невідома операція")
#
#     choice = input("Хочеш ще раз? (y/n): ")
#
#     if choice.lower() != "y":
#         print("Роботу завершено.")
#         break


# ДЗ 5.3. hashtag

# import string
#
# text = input("Введи текст: ")
#
# чистий_текст = ''
# for символ in text:
#     if символ not in string.punctuation and not символ.isspace():
#         чистий_текст += символ
#
# слова = text.split()
#
# хештег_слова = []
# for слово in слова:
#     нове = ''
#     for символ in слово:
#         if символ not in string.punctuation:
#             нове += символ
#     хештег_слова.append(нове.capitalize())
#
# хештег = '#' + ''.join(хештег_слова)
#
# if len(хештег) > 140:
#     хештег = хештег[:140]
#
# if хештег == '#':
#     print("#")
# else:
#     print(хештег)

























































# ДЗ 4.1. Перемістити всі нулі до кінця списку

# numbers = [0, 1, 0, 12, 3]
# new_list = []
# for number in numbers:
#     if number != 0:
#         new_list.append(number)
# for number in numbers:
#     if number == 0:
#         new_list.append(0)
# print(new_list)


# ДЗ 4.2. Знайти суму елементів із парними індексами
# numbers = [0, 1, 7, 2, 4, 8]
# if len(numbers) == 0:
#     print(0)
# else:
#     total = 0
#     for i in range(0, len(numbers), 2):
#         total += numbers[i]
#
#     result = total * numbers[-1]
#     print(result)




# ДЗ 4.3. Список із 3 елементів

# import random
# length = random.randint(3, 10)
# numbers = []
# for i in range(length):
#     numbers.append(random.randint(0, 100))
# print("Початковий список:", numbers)
#
# new_list = [numbers[0], numbers[2], numbers[-2]]
# print("Новий список:", new_list)




