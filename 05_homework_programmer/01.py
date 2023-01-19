# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

from encodings import utf_8

#в строке 7 необходимо прописать свою директорию

with open(r'F:\gitt\geek_brains\Python\05_homework_programmer\words.txt', encoding='utf_8') as my_file: 
    for line in my_file:
        words = line.split()
        for word in words:
            if 'абв' in word:
                words.remove(word)
        new_list = " ".join(words)
        print(new_list)