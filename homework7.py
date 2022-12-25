# 3. Даны списки my_list_1 и my_list_2. Создать список my_result
# в который вначале поместить элементы на четных местах из
# my_list_1, а потом все элементы на нечетных местах из my_list_2.

from random import randint

my_list_1=[]
my_list_2=[]

for i in range(10):
    my_list_1[i] = randint(1,400)
    my_list_2[i] = randint(1,400)
print(my_list_1)
print(my_list_2)

