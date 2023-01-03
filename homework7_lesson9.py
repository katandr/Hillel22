# 1)Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
#     а) Создать список и поместить туда имя самого молодого человека.
#         Если возраст совпадает - поместить все имена самых молодых.
#     б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
#     в) Посчитать среднее количество лет всех людей из начального списка.
#
# from statistics import mean
#
# persons = {
#     1: {
#         'name': 'John',
#         'age': 15
#     },
#     2: {
#         'name': 'Jack',
#         'age': 45
#     },
#     3: {
#         'name': 'Victor',
#         'age': 23
#     },
#     4: {
#         'name': 'Valery',
#         'age': 21
#     },
#    5: {
#         'name': 'Robert',
#         'age': 15
#     },
#     6: {
#         'name': 'Ben',
#         'age': 15
#     }
# }
# min_age=min(persons[id_person]['age'] for id_person in persons)
# print("min_age=",min_age)
# youngest_persons = []
#
# for id_person in persons:
#     if persons[id_person]['age'] == min_age:
#         youngest_persons.append(persons[id_person]['name'])
# print(youngest_persons)
# print("")
# longest_names = []
# longest_name_size = max(len(persons[id_person]['name']) for id_person in persons)
# print("longest_name_size = ",longest_name_size)
#
# for id_person in persons:
#     if len(persons[id_person]['name']) == longest_name_size:
#         longest_names.append(persons[id_person]['name'])
# print(longest_names)
#
# mean_age=mean(persons[id_person]['age'] for id_person in persons)
# print("среднее количество лет всех людей ",round(mean_age))



# 2)Даны два словаря my_dict_1 и my_dict_2.
#     а) Создать список из ключей, которые есть в обоих словарях.
#     б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
#     в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
#     г) Объединить эти два словаря в новый словарь по правилу:
#         если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
#         если ключ есть в двух словарях -
#         поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#         {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

my_dict_1 = {1:1, 2:2, 5:5, 7:7}
my_dict_2 = {11:11, 2:22, 1:56}
keys_my_dict_1 = list(my_dict_1.keys())
keys_my_dict_2 = list(my_dict_2.keys())

print(keys_my_dict_1)
print(keys_my_dict_2)

common_keys = []
for i in keys_my_dict_1:
    for j in keys_my_dict_2:
        if i == j:
            common_keys.append(i)
print(f"common_keys {common_keys}")

unique_keys_1 = []

for i in keys_my_dict_1:
    count = 0
    for j in keys_my_dict_2:
        if i != j:
            count += 1
    if count == len(keys_my_dict_2):
        unique_keys_1.append(i)

print(f"unique_keys_1 {unique_keys_1}")
dict_unique_keys1 = {x: my_dict_1[x] for x in unique_keys_1}
print(dict_unique_keys1)

print("my_dict_1", my_dict_1)
print("my_dict_2", my_dict_2)
combined_dict = my_dict_1.copy()
print("combined_dict_0:",combined_dict)
for i in my_dict_2:
    print(i)
    if i in combined_dict.keys():
        print("enter if")
        print(my_dict_2.get(i))
        print(combined_dict.get(i))
        values = [combined_dict.get(i),my_dict_2.get(i)]
        print(values)

    else:
        print("else",i)
        combined_dict.update(my_dict_2)

print("combined_dict ",combined_dict)
