# ДЗ 9.1

def popular_words(text, words):
    result = {}
    text = text.lower().split()

    for word in words:
        count = text.count(word)
        result[word] = count

    return result

# Тест
assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new''',
    ['i', 'was', 'three', 'near']
) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print('OK')



# ДЗ 9.2

# def difference(*args):
#     if not args:
#         return 0
#     return round(max(args) - min(args), 2)
#
# # Тести
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')



# ДЗ 10.1


# def pow(x):
#     return x ** 2
#
# def some_gen(begin, end, func):
#     current = begin
#     for _ in range(end + 1):
#         yield current
#         current = func(current)
#
# # Тестування
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')



# ДЗ 10.2

# def first_word(text):
#     text = text.replace('.', ' ').replace(',', ' ')
#     words = text.split()
#     return words[0]
#
# # Тести
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')


# ДЗ 10.3

# def is_even(digit):
#     """ Перевірка чи є парним число """
#     return digit % 2 == 0
#
# # Тести
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')


