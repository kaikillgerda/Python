# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071


number = int(input('Пожалуйста, введите количество чисел в списке -> '))
number_sum = 0
list_num = []


for i in range(1, number+1):
    res = round((1+1/i)**i, 3)
    list_num.append(res)
    number_sum = number_sum + res


print(list_num)    
print('Сумма чисел равна - >', number_sum)