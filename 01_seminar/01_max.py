# является ли одно число квадратом второго и наоборот

print('Введите a')
a = int(input())
print('Введите b')
b = int(input())
if a**2 == b or b**2 == a:
    print('yes')
else:
    print('no')


first_user_number = int(input(' Enter first number: '))
second_user_number = int(input(' Enter second number: '))
print(f'{first_user_number}, {second_user_number} ->', end=' ')

if first_user_number == second_user_number ** 2 or second_user_number == first_user_number ** 2:
    print('yes')
else:
    print('no')


numbers = [1, 4, 6, 2, 3]
for i in range(1, 6):
numbers.append(int(input(f'Введите элемент под номером {i}: ')))
print(numbers)
print(max(numbers))



my_max = 0
for _ in range(5):
    num = int(input('Введите число: '))
    if my_max < num:
        my_max = num

print(my_max)


от -N до N
n = int(input('Введите число'))
if n < 0:
    n *= -1
for i in range(-n, n+1):
    print(i, end=' ')



num = input('enter number: ')
if '.' in num:
    index_num = num.find('.')+1
    print(num[index_num])
elif ',' in num:
    index_num = num.find(',')+1
    print(num[index_num])
else:
    print('no')



num = input('Введите дробное число: ')
if num.isdigit():
    print('нет')
else:
    num = int(float(num)*10 % 10)
    print(num)
