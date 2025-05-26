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

import random
length = random.randint(3, 10)
numbers = []
for i in range(length):
    numbers.append(random.randint(0, 100))
print("Початковий список:", numbers)

new_list = [numbers[0], numbers[2], numbers[-2]]
print("Новий список:", new_list)




