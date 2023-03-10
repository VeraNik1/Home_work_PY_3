# Домашняя работа Семинар 3
# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, 
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 3

# 1 2 3 4 5
# Вывод: 1


import random

while True:
    try:
        N = int(input("Введите длину массива >>> "))
        if N > 0:
            break
        else:
            raise Exception

    except:
        print('Вы ввели не натуральное число, попробуйте еще раз')

A = [random.randint(1, N // 2 + N % 2) for _ in range(N)]
print('массив:', A)
while True:
    try:
        X = int(input('Введите целое число X, количество которого будем искать в массиве А>>> '))
        break
    except:
        print('Вы ввели не целое число, попробуйте еще раз')
print(f'Число X = {X} встречается в массиве A {A.count(X)} раз(а)\n')

# Задача 18:

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший.

# Ввод: 5
# Ввод: 6
# 1 2 0 4 7
# Вывод: 7

import random

while True:
    try:
        N18 = int(input('Введите длину массива >>> '))
        if N18 > 0:
            break
        else:
            raise Exception

    except:
        print('Вы ввели не натуральное число, попробуйте еще раз')


A18 = [random.randint(1, N18 // 2 + N18 % 2) for _ in range(N18)] 
print('массив:', A18)
while True:
    try:
        X18 = int(input('Введите число X, которое необходимо проверить>>> '))
        break
    except:
        print('Вы ввели не целое число, попробуйте еще раз')

Dict = {k: abs(k - X18) for k in set(A18)}
min_value = (min(Dict.values()))
res = []
for k, v in Dict.items():
    if v == min_value:
        res.append(k)
print(f"Ближайшее к Х = {X18} наименьшее число в массиве: {min(res)}")



# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12
def points(num):
    if num % 100 in [11, 12, 13, 14]:
        return 'очков'
    elif num % 10 == 1:
        return 'очко'
    elif num % 10 in [2, 3, 4]:
        return 'очка'
    else:
        return 'очков'

def correct_lang(word):
    if word.isalpha() and ((all(x.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for x in word) \
       or all(not x.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for x in word))):
       return True
    else:
        return False

data = {'AEIOULNSTRАВЕИНОРСТ': 1, 'DGДКЛМПУ': 2, 'БГЁЬЯBCMP': 3, 'FHVWYЙЫ': 4, 'KЖЗХЦЧ': 5, 'JXФЩЪ': 8, 'QZФЩЪ': 10}
result = 0

while True:
    word = input('Введите слово для рачета стоимости>>> ')
    if correct_lang(word):
        break
    else:
        print("Пожалуйста, используйте при вводе ТОЛЬКО буквы русского или ТОЛЬКО английского алфавита!")
        
for letter in word:
    for k in data.keys():
        if letter.upper() in k:
            result += data[k]
            break

print(f'слово {word} стоит {result} {points(result)}')


