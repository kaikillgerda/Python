# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Пожалуйста, введите вещественное число -> ')
degree = len(number) - 2
number = float(number)
number = number * (10 ** degree)
if float(number) < 0:
    number = number * (-1)

digit_sum = 0

while number:
    digit_sum = digit_sum + number % 10
    number = number//10

print('Сумма цифр заданного числа равна -> ', int(digit_sum))
