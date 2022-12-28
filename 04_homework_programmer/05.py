# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


first_file1 = open('file1.txt', 'r')
first_file2 = open('file2.txt', 'r')
first_file3 = open('file3.txt', 'w')
file1 = first_file1.readline()
file2 = first_file2.readline()
for i in range(len(file1)):
    if file1[i-1] != '^':
        if file1[i].isnumeric():
            first_file3.write(str(int(file1[i])+int(file2[i])))
        else:
            first_file3.write(str(file1[i]))
    else:
        first_file3.write(str(file1[i]))
first_file1.close
first_file2.close
first_file3.close