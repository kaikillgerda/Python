# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

number = int(input('Пожалуйста, введите значение количества элементов -> '))



list_num = list(range(-number, number + 1))
print(list_num)

data = open('file.txt', 'w')
pos_1 = input('Пожалуйста, введите позицию первого числа -> ')
pos_2 = input('Пожалуйста, введите позицию второго числа -> ')
data.write(pos_1+'\n')
data.write(pos_2)
data.close

list_len = len(list_num)

pos_1 = int(pos_1)
pos_2 = int(pos_2)

if list_len >= pos_1 > 0 and list_len >= pos_2 > 0:
    print(list_num[pos_1 - 1] * list_num[pos_2 - 1])
else:
    print('Ошибка! Введенные позиции отсутствуют в заданном списке')
