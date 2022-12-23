# задача 1
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# print('Введите числа списка через пробел:' , end = " ")
# n = input()
# summ = 0
# list = list(map(int, n.split(" ")))
# print(list)
# for i in range(1, len(list), 2):
#     summ += list[i]
# print(summ)

# задача 2
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# print('Введите числа списка через пробел:' , end = " ")
# n = input()
# result_list = []
# list = list(map(int, n.split(" ")))
# print(list)
# if len(list)%2 == 0:
#     for i in range(len(list)//2):
#         result_list.append(list[i] * list[len(list) - 1 - i])
# else:
#     for i in range(round(len(list)//2) + 1):
#         result_list.append(list[i] * list[len(list) - 1 - i])
# print(result_list)

# задача 3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# list = list(map(float, input("Введите числа через пробел:\n").split()))
# new_list = []
# for i in list:
#     if i%1 != 0:
#         new_list.append(round(i%1, 2))
# print(max(new_list) - min(new_list))

# задача 4
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input('Введите число: '))
# bin = ""
# while n != 0:
#     bin = str(n%2) + bin
#     n //= 2
# print(bin)

# задача 4
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# fib_1 = fib_2 = 1
# n = abs(int(input()))
# fib_n = [fib_1, fib_2] 
# for i in range(2, n):
#     fib_1, fib_2 = fib_2, fib_1 + fib_2
#     fib_n.append(fib_2)
# fib_n.insert(0, 0)
# n_fib = []
# for i in range(1, len(fib_n)):
#     if i%2 == 0: 
#         n_fib.append(fib_n[i] * -1)
#     else:
#         n_fib.append(fib_n[i])
# for i in range(len(n_fib)):
#     fib_n.insert(0, n_fib[i])
# print(fib_n)