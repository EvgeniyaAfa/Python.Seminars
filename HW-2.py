import random

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
2

# q_coin = int(input("Input quantity of coins: "))
#
#
# count_reshka = 0
# count_orel = 0
# for i in range(q_coin):
#     coin = random.randint(0, 1)
#     print(coin)
#     if coin == 1:
#         count_orel += 1
#     else:
#         count_reshka += 1
# if count_orel > count_reshka:
#
#  print(f"Min coins are {count_reshka}")
# else:
#
#  print((f"Min coins are {count_orel}"))

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 * 3
# diggit_one = int(input("Назови первое число:  "))
# diggit_two = int(input("Назови второе число:  "))
#
#
# summa = diggit_one + diggit_two
# proizvedenie = diggit_one * diggit_two
# i = 0
# while i < diggit_one and i < diggit_two:
#  i += 1
# if diggit_one == summa - diggit_two and diggit_two == proizvedenie // diggit_one and diggit_two == summa - diggit_one and diggit_one == proizvedenie // diggit_two:
#     print(f"{summa} = {diggit_one} + {diggit_two} и {proizvedenie} = {diggit_one} * {diggit_two}")
# else:
#     print(f"Подумай еще")

# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# number = int(input("Введите число n: "))
#
# i = 1
# while i <= number:
#     print(2 ** i)
#     i += 1