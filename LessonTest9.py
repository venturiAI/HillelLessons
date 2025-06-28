# ДЗ 12.1

import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    clean_text = re.sub(r'<.*?>', '', html)
    lines = clean_text.split('\n')
    non_empty_lines = [line.strip() for line in lines if line.strip() != '']
    final_text = '\n'.join(non_empty_lines)
    with codecs.open(result_file, 'w', 'utf-8') as result:
        result.write(final_text)

    print(f"Готово! Текст записано у файл '{result_file}'")


# ДЗ 12.2

# class Item:
#     def __init__(self, name, price, description, dimensions):
#         self.name = name
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#
#     def __str__(self):
#         return f"{self.name}, price: {self.price}"
#
#
# class User:
#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone
#
#     def __str__(self):
#         return f"{self.name} {self.surname}"
# 
#
# class Purchase:
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#
#     def add_item(self, item, cnt):
#         self.products[item] = cnt
#
#     def get_total(self):
#         total = 0
#         for item, count in self.products.items():
#             total += item.price * count
#         return total
#
#     def __str__(self):
#         result = f"User: {self.user}\nItems:\n"
#         for item, count in self.products.items():
#             result += f"{item.name}: {count} pcs.\n"
#         return result.strip()
