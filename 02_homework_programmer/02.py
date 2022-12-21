# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Пожалуйста, введите число -> '))
digit = 1
list_num = []

for i in range(number):
    digit = digit * (i + 1)
    list_num.append(digit)

print(list_num)
