"""
Пользователь вводит с клавиатуры три числа в переменные a, b, c. Найдите наибольшее число из них и запишите в переменную max.
"""

a1 = int(input())
b1 = int(input())
c1 = int(input())
if a1 > b1 and a1 > c1:
    print(a1)
elif b1 > a1 and b1 > c1:
    print(b1)
else:
    print(c1)