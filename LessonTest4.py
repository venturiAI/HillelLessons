# ДЗ 6.1

import string

s = input()
start, end = s.split("-")
letters = string.ascii_letters
i1 = letters.index(start)
i2 = letters.index(end)
print(letters[i1:i2 + 1])


# ДЗ 6.2

# s = int(input())
#
# d = s // 86400
# s = s % 86400
#
# h = s // 3600
# s = s % 3600
#
# m = s // 60
# s = s % 60
#
# print(f"{d} днів, {str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}")


# ДЗ 6.3

# n = int(input())
#
# while n > 9:
#     result = 1
#     for digit in str(n):
#         result *= int(digit)
#     n = result
#
# print(n)
