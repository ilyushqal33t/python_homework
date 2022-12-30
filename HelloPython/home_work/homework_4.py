# 1 Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import math
# d = input('d:')
# n = input('Введите десятичную дробь:')
# d_list = list(d.split("."))
# n_list = list(n.split("."))
# accuracy = len(d_list[1])
# print(n_list[0] + '.' + n_list[1][0:accuracy])

# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

# n = int(input('Введите натуральное число:'))
# multiplier_list = []
# denominator = 2
# while n != 1:
#     if n % denominator == 0:
#         n /= denominator
#         multiplier_list.append(denominator)
#     else:
#         denominator += 1
# print(multiplier_list)

# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

# import random
# rnd_list = [random.randint(0, 10) for i in range(random.randint(5, 15))]
# print(rnd_list)
# result_list = [i for i in rnd_list if rnd_list.count(i) == 1]
# print(result_list)

# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
# k = int(input('Введите натуральную степень k: '))
# coef_list = [random.randint(0,100) for i in range(k+1)]
# print(coef_list)
# path = 'polynomial.txt'
# with open(path, 'w') as data:
#     for i in range(k, -1, -1):
#         if coef_list[i] == 0:
#             continue
#         data.write(str(coef_list[i]) + ('*x' if i!=0 else ''))
#         data.write(('**'+str(i)) if i > 1 else '')
#         data.write('+' if i!=0 else '')
#     data.write('=0')

# 5 Задача.
# import random
# def polynomial(k, path):
#     coef_list = [random.randint(0,100) for i in range(k+1)]
#     print(coef_list)
#     with open(path, 'w') as data:
#         for i in range(k, -1, -1):
#             if coef_list[i] == 0:
#                 continue
#             data.write(str(coef_list[i]) + ('*x' if i!=0 else ''))
#             data.write(('**'+str(i)) if i > 1 else '')
#             data.write('+' if i!=0 else '')
#         data.write('=0')

# k1 = int(input('Введите натуральную степень k для первого многочлена: '))
# k2 = int(input('Введите натуральную степень k для второго многочлена: '))
# polynomial(k1, 'polinomial_1.txt')
# polynomial(k2, 'polinomial_2.txt')