1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
    *Пример:*
    
    - Для N = 5: 1, -3, 9, -27, 81
2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
    *Пример:*
    
    - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.


# 1
import random # взяли из гугля
n = int(input('Print your N: '))
for i in range(n):
    print(random.randint(0,10), end=' ')

n = int(input('Введите натруальное число N: '))
list = []
for i in range(1, n+1):
    elem = 3*i + 1
    list.append(elem)
print(list)


import random

num = int(input("Ведите число: ")) #   = 5

a = []
for i in range(num):
    a.append(random.randint(-10,10) )

print(a)


# 2


n = int(input('Print your N: '))
my_dict = {}

for i in range(1,n+1):
    my_dict[i] = 3*i + 1
print(my_dict)


