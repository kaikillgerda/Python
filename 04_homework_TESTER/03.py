# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


from random import randint


N = int(input())
list = []
for i in range(1,N+1):
    a = randint(-N,N+1)
    list.append(a)
print(list)

newlist = []
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist)