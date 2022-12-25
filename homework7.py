# 3. Даны списки my_list_1 и my_list_2. Создать список my_result
# в который вначале поместить элементы на четных местах из
# my_list_1, а потом все элементы на нечетных местах из my_list_2.

from random import randint
my_result = []
my_list_1 = [randint(1,100) for x in range(10)]
my_list_2 = [randint(1,100) for x in range(10)]
my_result = my_list_2
print("my_list_1",my_list_1)
print("my_list_2",my_list_2)

for i in range (1,20,2):
    my_result.insert(i,my_list_1.pop(0))
print(my_result)

#
# 11. Дана строка my_str. Создать список в который поместить те символы из my_str, которые встречаются
# в строке ТОЛЬКО ОДИН раз.

my_str = "this is the the first and the last string number twenty"
list=[]
count=0
for i in range(len(my_str)):
    count = 0
    for y in range(len(my_str)):
        if my_str[i] == my_str[y]:
            count+=1
    if count == 1:
        list.append(my_str[i])

print(list)

