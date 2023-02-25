#____________________Seminar-5_____________________________
#Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи

# def fibonachi (number):
#     if number in [1, 2]:
#         return 1
#     return fibonachi(number - 1) + fibonachi(number - 2)

# print(fibonachi(int(input("Input your number "))))   

# Василий получил доступ к классному журналу и хочет заменить все свои
# минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки 
# Василия, но наоборот: все максимальные – на минимальные    


# import random
# list_mark = []  ## пустой список
# max_mark = 10 ## максимальное кол-во оценок
# for i in range(max_mark):         ##циклом бежим до конца списка
#     list_mark.append(random.randint(1, 5)) ## добавляем  в список рандомное число из диапазона
# print(list_mark)    

# new_mark = []   ## новый
# for i in range(len(list_mark)):
#     if i >= 4:
#         new_mark.append(random.randint(1, 3))
#     elif i <= 3:
#         new_mark.append(random.randint(1, 3)) 
# print(new_mark)



# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)*

# def similar_or_not (number: int) -> bool:
#     for i in range(3, number,2):
#         if number % i == 0:
#          return False
#     return True     

# n = int(input("Input your number:   "))

# print(similar_or_not(n))         

#________________________________________________________________HOME WORK_____________________
# 1.Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# num1 = int(input("Input first number:     "))
# num2 =  int(input("Input second number:   "))

# def stepen (a, b):
#  if b > 0:
#      return a * stepen(a, b - 1)
#  else:
#      return 1
  
# print(stepen(num1,num2))          

# 2.Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# num1 = int(input("Input first number:  "))
# num2 = int(input("Input second number:  "))

# def rec_sum (a, b):
#     if b == 0:
#         return a
#     return rec_sum(a + 1, b -1)
# print(rec_sum(num1,num2))

           