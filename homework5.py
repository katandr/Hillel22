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
height=int(input("введите высоту="))
rows = height -1
print("========Figure 1=========")
for x in range(0,rows):
    for y in range(x,rows):
         print(" ", end=" ")

    print("*", end=" ")

    for t in range((x*2-1)):
        print(" ", end=" ")
    if x>0:
        print("*", end=" ")

    for i in range(x,rows):
        print(" ", end=" ")
    print(" ")

    if x == rows-1:
        for j in range(rows*2+1):
            print("*", end=" ")

print("\n\n========Figure 2=========")
for x in range(0,rows):
    for y in range(x,rows):
         print(" ", end=" ")

    print("*", end=" ")

    for t in range((x*2-1)):
        print("*", end=" ")
    if x>0:
        print("*", end=" ")

    for i in range(x,rows):
        print(" ", end=" ")
    print(" ")

    if x == rows-1:
        for j in range(rows*2+1):
            print("*", end=" ")


print("\n\n========Figure 3=========")

for x in range(0,rows):
    for y in range(x,rows):
         print(" ", end=" ")

    print("*", end=" ")

    for t in range((x*2-1)):
        print("*", end=" ")
    if x>0:
        print("*", end=" ")

    for i in range(x,rows):
        print(" ", end=" ")
    print(" ")

    if x == rows-1:
        for j in range(rows*2+1):
            print("*", end=" ")
print("")

for x in range(rows,0,-1):
    for y in range(x,rows+1):
         print(" ", end=" ")

    print("*", end=" ")

    for t in range((x*2-3)):
        print(" ", end=" ")
    if x !=1:
        print("*", end=" ")

    for i in range(x,rows+1):
        print(" ", end=" ")
    print(" ")


print("\n\n========Figure 4=========")

for x in range(0,rows):
    for y in range(x,rows):
         print(" ", end=" ")

    print("*", end=" ")

    for t in range((x*2-1)):
        print("*", end=" ")
    if x>0:
        print("*", end=" ")

    for i in range(x,rows):
        print(" ", end=" ")
    print(" ")

    if x == rows-1:
        for j in range(rows*2+1):
            print("*", end=" ")
print("")

for x in range(rows,0,-1):
    for y in range(x,rows+1):
         print(" ", end=" ")

    print("*", end=" ")

    for t in range((x*2-3)):
        if t == x-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    if x !=1:
        print("*", end=" ")

    for i in range(x,rows+1):
        print(" ", end=" ")
    print(" ")

