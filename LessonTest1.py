# ДЗ 2.1 Виведення числа в стовпчик


# CHATGPT только освежил знания уже несколько раз пройденного материала и дал примеры с реализацией divmod, остальное я соединил и реализовал. Процентов 70% моей заслуги, но навряд ли я такое смогу написать с нуля. Понимание есть, а реализацию нужно больше практиковать.
#Из того что я увидел и взял на заметку 1000  <= user_numbers <= 9999
user_numbers = int(input("Write a four-digit number\n"))
if 1000  <= user_numbers <= 9999 and len(str(user_numbers)) == 4:
    thousands, remainder = divmod(user_numbers, 1000)
    hundreds, remainder = divmod(remainder, 100)
    tens, ones = divmod(remainder, 10)

    print(thousands)
    print(hundreds)
    print(tens)
    print(ones)
else:
    print("This is not a four digit number!")


# упрощенный пример

number = int(input("Enter number: "))
if number >= 1000 and number <= 9999:
    a = number // 1000
    b = number % 1000
    c = b // 100
    d = b % 100
    e = d // 10
    f = d % 10

    print(a)
    print(c)
    print(e)
    print(f)
else:
    print("Not 4 digit")


# ДЗ 2.2

number = int(input("Введіть 5-значне число: "))
reversed_number = 0

reversed_number = reversed_number * 10 + number % 10
number = number // 10

reversed_number = reversed_number * 10 + number % 10
number = number // 10

reversed_number = reversed_number * 10 + number % 10
number = number // 10

reversed_number = reversed_number * 10 + number % 10
number = number // 10

reversed_number = reversed_number * 10 + number % 10
number = number // 10

print("Перевернуте число:", reversed_number)
