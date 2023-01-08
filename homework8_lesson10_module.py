# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

def string_odd_change(my_list) -> list:
    """
        Функция возвращает новый список в котором содержаться элементы из my_list по следующему правилу:
        Если строка стоит на нечетном месте в my_list, то ее заменить на перевернутую строку. "qwe" на "ewq".
        Если на четном - оставить без изменения
        :return: new string
        """
    print(f'initial list     {my_list}')
    new_list=[]
    for i in range(len(my_list)):
        if i % 2 == 0:
            reverse_string = my_list[i][::-1]
            new_list.append(reverse_string)

        else:
            new_list.append(my_list[i])
    print(f'transformed list {new_list}')
    return(new_list)

def first_a(my_list) -> list:
    """
        Функция возвращает новый список в котором содержаться
элементы из my_list у которых первый символ - буква "a".
        :return: new string
    """
    print(f'initial list {my_list}')
    new_list=[]
    for i in my_list:
        if i.find('a') == 0:
            new_list.append(i)

    print(f'new list {new_list}')
    return (new_list)