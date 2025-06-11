# ДЗ 7.1

def say_hi(name, age):
    return "Hi. My name is " + name + " and I'm " + str(age) + " years old"

# Тести
assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')


# ДЗ 7.2

# def correct_sentence(text):
#     text = text[0].upper() + text[1:]
#     if not text.endswith("."):
#         text += "."
#     return text
#
# # Тести
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')



# ДЗ 7.3

# def second_index(text, some_str):
#     first = text.find(some_str)
#     if first == -1:
#         return None
#     second = text.find(some_str, first + 1)
#     if second == -1:
#         return None
#     return second
#
# # Тести
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')


# ДЗ 7.4

# def common_elements():
#     list1 = [x for x in range(100) if x % 3 == 0]
#     list2 = [x for x in range(100) if x % 5 == 0]
#     return set(list1) & set(list2)
#
# # Тест
# assert common_elements() == {0, 15, 30, 45, 60, 75, 90}
# print("ОК")
