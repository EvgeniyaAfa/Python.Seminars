#Задаем длину списка наполненного рандомными числами от 1 до 100.
#Вводим искомое число X
#Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
#которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению



# from random import randint as rand
#
# size = int(input('Введите длину списка: '))
# x = int(input('Введите искомое число: '))
#
# list_1 = [rand(1, 10) for _ in range(size)]
# print(list_1)
# if list_1.count(x) == 0:
#     nearest = list_1[0]
#     for item in list_1:
#         if abs(x - item) < abs(x - nearest):
#             nearest = item
#     print(f"Ближайшее число это {nearest}")
# else:
#     print(f"В списке {list_1}, искомое число встречается {list_1.count(x)} раз")
#
# #A, E, I, O, U, L, N, S, T, R – 1 очко;
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
# Ф, Щ, Ъ – 10 очков

dict = {1: 'AEIOULNSTRАВЕИНОРСТ',
           2: 'DGДКЛМПУ',
           3: 'BCMPБГЁЬЯ',
           4: 'FHVWYЙЫ',
           5: 'KЖЗХЦЧ',
           8: 'JXШЭЮ',
           10: 'QZФЩЪ'}
word = str(input("Введите слово: "))
sum = 0
for item in word:
    for key, value in dict.items():
        if item.upper() in value:
            sum += key
print(f"Сумма букв в {word} = {sum}")