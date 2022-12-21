# Реализуйте алгоритм перемешивания списка

from random import randrange
num = int(input('Пожалуйста, введите число -> '))
list_num = list(range(num))

print(list_num)

for i in list_num:
    num_1, num_2 = randrange(num), randrange(num)
    list_num[num_1], list_num[num_2] = list_num[num_2], list_num[num_1]

print(list_num)
