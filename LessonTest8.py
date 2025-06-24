# Дз 11.1
def prime_generator(end):
    for num in range(2, end + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num


#ДЗ 11.2

# def generate_cube_numbers(end):
#     number = 2
#     while True:
#         cube = number ** 3
#         if cube > end:
#             return
#         yield cube
#         number += 1


#ДЗ 11.3

# def is_even(number):
#     return (number & 1) == 0