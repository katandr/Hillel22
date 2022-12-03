# 1. Написать калькулятор для простых операций(+,-,*,/,**),
# Операнды и оператор вводятся с клавиатуры отдельно(отдельные переменные)


number1 = int(input("введите первое число  "))
number2 = int(input("ввесдите второе число  "))
operation = input("ввесдите операцию +,-,*, /, **  ")

if operation == "+":
    print(f"{number1} + {number2} = {number1+number2}")
elif operation == "-":
    print(f"{number1} - {number2} = {number1-number2}")
elif operation == "*":
    print(f"{number1} * {number2} = {number1 * number2}")
elif operation == "/":
    print(f"{number1} / {number2} = {number1 / number2}")
elif operation == "**":
    print(f"{number1} ** {number2} = {number1 ** number2}")


# 2. По данному целому числу N распечатайте все квадраты натуральных чисел,
#  не превосходящие N, в порядке возрастания.
# Например:
# 50      1 4 9 16 25 36 49
# 10      1 4 9
# 100     1 4 9 16 25 36 49 64 81 100

N = int(input("введите целое число N  "))
square=1
for i in range (N):
    if i**2 <=N:
        print(f"{i**2}", sep="\t", end=" ")


# 3. Определить является ли введенное с клавиатуры число простым
# (делится без остатка только на себя и единицу)

number = int(input("введите число_"))

simple= True
for i in range(2,number):
    if number % i == 0:
        simple = False
if simple:
    print("простое")
else:
    print("число не является простым")


# Создайте приложение подбирающее правильное окончание к фразе:
#  "Маша нашла в лесу {К} гриб...". K пользователь вводит с клавиатуры.
# Например: Маша нашла в лесу 7 грибОВ.
# Маша нашла в лесу 32 грибА.
K = int(input("сколько грибов нашла Маша в лесу "))
ending=""
if (K % 10) == 0 or (K % 10) in range(5,10) or (K == 11):
    ending="ов"
elif (K % 10) == 1:
    ending=""
elif (K % 10) in range(2,5):
    ending="а"

print(f"Маша нашла в лесу {K} гриб{ending}")
