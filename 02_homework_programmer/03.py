# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input('Пожалуйста, введите количество чисел в списке -> '))
number_sum = 0
list_num = []

for i in range(1, number+1):
    res = round((1+1/i)**i, 3)
    list_num.append(res)
    number_sum = number_sum + res

print(list_num)    
print('Сумма чисел равна - >', number_sum)