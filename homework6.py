# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

from random import randint
my_list = [randint(1,300) for i in range(10)]
print(my_list)
for i in my_list:
    if i>100:
        print(i, end = " ")

# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

from random import randint
my_list = [randint(1,300) for i in range(10)]
print("my_list:", my_list)
my_results = list()
for i in my_list:
    if i>100:
        my_results.append(i)
print("my_results:",my_results)

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


# *4. Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k,
#  сдвинув влево все элементы, стоящие правее элемента с индексом k.
# 	- Программа получает на вход список (можно сгенерировать при помощи генератора случайных чисел),
# 	 затем число k. Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop()
# 	 без параметров.
# 	- Программа должна осуществлять сдвиг непосредственно в списке,
# 	 а не делать это при выводе элементов. Также нельзя использовать дополнительный список.
# 	  Также не следует использовать метод pop(k) с параметром или оператор del.

from random import randint

my_list = [randint(1,300) for i in range(randint(3,10))]
print("my_list:     ", my_list)
k = int(input("enter k:"))
for i in range(k,len(my_list)-1):
    my_list[i] = my_list[i+1]
my_list.pop()
print(my_list)


# *5. Дан список целых чисел (можно сгенерировать при помощи генератора случайных чисел),
#  число k и значение C. Необходимо вставить в список на позицию с индексом k значение C,
#   сдвинув все элементы, с индексом большим k, вправо. Поскольку при этом количество элементов в списке увеличивается,
#   в конец списка нужно будет добавить новый элемент (любое значение), используя метод append().
# 	- Вставку необходимо осуществлять уже в считанном списке,
# 	 не делая этого при выводе и не создавая дополнительного списка.
# 	- Использовать метод insert() не разрешается.

from random import randint

my_list = [randint(1,300) for i in range(randint(3,10))]
print("my_list:    ", my_list)

while True:
    k = int(input("enter k:"))
    if k > len(my_list):
        print("k is not valid, please try again")
    else:
        break

c = int(input("enter c:"))
my_list.append(0)

for i in range(len(my_list)-1,k,-1):
    my_list[i] = my_list[i-1]
my_list[k]=c
print("updated list: ", my_list)

# *6. Даны два списка чисел (можно сгенерировать при помощи генератора случайных чисел).
#  Посчитайте, сколько уникальных чисел содержится одновременно как в первом списке, так и во втором.
# 	- Примечание. Эту задачу можно решить в одну строчку.


# #  Последнее задание не сделано, хочу обсудить с Вами до урока,
# здесь оставляю попытку выполнения, что бы было о чем поговорить

# #from random import randint

# # my_list1 = [randint(1,300) for i in range(randint(3,10))]
# # print("my_list1:    ", my_list1)
# # my_list2 = [randint(1,300) for i in range(randint(3,10))]
# # print("my_list1:    ", my_list2)
# my_list1 = [1,1,14,1]
# my_list2 = [2,2,2]
# my_list3 = list()
# my_list3=[i for i in (my_list1+my_list2) if i not in my_list3]
# print("my_list3: ",my_list3)
# len(my_list3)
