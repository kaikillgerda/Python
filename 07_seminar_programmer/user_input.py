num_1 = 0
num_2 = 0
oper = ''


def inp():
    global num_1
    global num_2
    global oper
    num_1 = float(input('Введите число 1 -> '))
    num_2 = float(input('Введите число 2 -> '))
    oper = input('Введите оператор: * или / или + или -: ')
    return (num_1, num_2, oper)

# # Нужно доработать с комплексными
# def prompt():
#     print('С каким типом данных будем работать?')
#     while True:
#         us_in = int(input('0 - комплексные, 1 - вещественные'))
#         if us_in == 0 or us_in == 1:
#             return us_in
#         print('Некорректный ввод! Повторите ввод данных!')
