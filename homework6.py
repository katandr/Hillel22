# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

# from random import randint
# my_list = [randint(1,300) for i in range(10)]
# print(my_list)
# for i in my_list:
#     if i>100:
#         print(i, end = " ")

# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

# from random import randint
# my_list = [randint(1,300) for i in range(10)]
# print("my_list:", my_list)
# my_results = list()
# for i in my_list:
#     if i>100:
#         my_results.append(i)
# print("my_results:",my_results)

#
# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

from random import randint

my_list = [randint(1,300) for i in range(randint(1,10))]
print("my_list:     ", my_list)
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1]+my_list[-2])
print(" ")
print("updated list:",my_list)


