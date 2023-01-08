import random
import string

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

    return (new_list)

def anywhere_a(my_list) -> list:
    """
        Функция возвращает новый список в котором содержаться
элементы из my_list в которых есть символ - буква "a" на любом месте.
        :return: new string
    """
    print(f'initial list {my_list}')
    new_list=[]
    for i in my_list:
        if 'a'in i:
            new_list.append(i)
    return (new_list)

def only_strings(my_list) -> list:
    """
        Функция возвращает новый список в котором содержаться только строки из my_list.
        :return: new string
    """
    print(f'initial list {my_list}')
    new_list=[]
    for i in my_list:
        if type(i) == str:
            new_list.append(i)
    return (new_list)

def unique_chars(my_str) -> list:
    """
    Функция возвращает новый список в котором содержаться те символы из my_str,
    которые встречаются в строке только один раз.
    """
    print(f'initial string {my_str}')
    new_list=[]
    for char in my_str:
        count=0
        for i in my_str:
            if char == i:
                count+=1
        if count == 1:
            new_list.append(char)
    return new_list

def compare_strings(my_str1:str, my_str2:str) -> list:
    """
    Функция возвращает список в который поместить те символы,
которые есть в обеих строках хотя бы раз.
    :param my_str1: 
    :param my_str2: 
    :return: new string
    """
    print(f'initial string 1 {my_str1}')
    print(f'initial string 2 {my_str2}')
    new_list = []
    for i in my_str1:
        count=0
        for j in my_str2:
            if i==j:
                count+=1
        if count>0:
            new_list.append(i)
    return new_list

def compare_strings_unque_char(my_str1:str,my_str2:str) ->list:
    """
    Функция возвращает список в который поместить те символы, которые есть в обеих строках,
но в каждой только по одному разу.
    :param my_str1: 
    :param my_str2: 
    :return: new list
    """
    print(f'initial string 1 {my_str1}')
    print(f'initial string 2 {my_str2}')
    new_list = []
    for i in my_str1:
        count = 0
        for j in my_str2:
            if i == j:
                count += 1
        if count == 1:
            new_list.append(i)
    return new_list

def generate_email(names:list,domains:list) ->str:
    """
    функцию для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.

    :param names:
    :param domains:
    :return: generated email as string
    """

    email = ''
    random_string = ''
    number_of_names = len(names)
    number_of_domains = len(domains)
    name = names[random.randrange(number_of_names)]
    domain = domains[random.randrange(number_of_domains)]
    number = random.randrange(100,999)
    random_string =''.join(random.choice(string.ascii_lowercase) for i in range(random.randrange(5,8)))

    email = name+'.'+str(number)+'@'+random_string+'.'+domain

    return email
