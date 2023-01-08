import homework8_lesson10_module as hw8

my_list = ['qwae','ett','aer','frr','art','axc']
my_list2 = ['qwae','ett',456, 56,'aer','frr',67, 'art','axc']
my_str = 'dtyuytrtyunasas'
my_str1 = 'qwrtypk'
my_str2 = 'qaqqwolpp'
names = ['smith','robinson','black','bush','klinton']
domains = ['google','yahoo','microsoft','tiktok']
def main():
    print(f'transformed list {hw8.string_odd_change(my_list)}')
    print("")
    print(f'new list with string begin with a {hw8.first_a(my_list)}')
    print("")
    print(f'new list with a in the string {hw8.anywhere_a(my_list)}')
    print("")
    print(f'new list with strings only {hw8.only_strings(my_list2)}')
    print("")
    print(f'new list with unique char {hw8.unique_chars(my_str)}')
    print("")
    print(f'new list with unique char {hw8.compare_strings(my_str1,my_str2)}')
    print("")
    print(f'new list with unique char {hw8.compare_strings_unque_char(my_str1, my_str2)}')
    print("")
    print(f'generated email: {hw8.generate_email(names,domains)}')

main()


