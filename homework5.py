# 1)У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и распечатать их.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.

my_string = '0123456789'
i = 0
y = 0
while i < 10:
    first = my_string[i]
    i+=1
    while y < 10:
        second = my_string[y]
        print(first+second)
        y += 1
    y=0


# При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
# представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.
# height = input("введите высоту ")
# A
#             *
#           *   *
#         *       *
#       *           *
#     *               *
#   *                   *
# * * * * * * * * * * * * *
