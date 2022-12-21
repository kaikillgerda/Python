# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного 
# генератора псевдослучайных чисел.

import time

ct = time.time()
rn = 9999 * ct
print(str(round(rn % 100)))


current_time = time.time()
print(current_time)
rand_num = int(1000 * current_time)
print(rand_num)
print(rand_num % 100)
print(str(rand_num)[-5:])

# 2. Задайте список. Напишите программу, которая определит, присутствует ли в 
# заданном списке строк некое число.

import os
os.system("cls")

list1 = ['2' , '3' , '4' , '5']
x = (input("Введите число: "))

for i in list1:
    if x == i:
        print(f'да, есть число {i} в списке')
        break
else:
    print("нет числа в списке")




my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
print(my_list)

string_find = "йу"
count = -1
for i in range(len(my_list)):
    if string_find == my_list[i]:
        count+=1
        if count == 1:
            count = i
            print(i)
            break
else:
    print(count)
