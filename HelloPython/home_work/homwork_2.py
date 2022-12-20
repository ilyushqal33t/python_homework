# задача 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# print('Введите число: ', end = "")
# num = int(input())
# sum = 0
# while num > 0:
#     sum += num % 10
#     num //= 10
# print(sum)

# задача 2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
# print('Введите число: ', end = "")
# n = int(input())
# list = []
# multpl = 1
# for i in range(1, n+1):
#     list.append(multpl * i)
#     multpl *= i
# print(list)

# задача 3
# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму
# print('Введите число: ', end = "")
# n = int(input())
# list = []
# sum = 0
# for i in range(1, n+1):
#     list.append(round((1 + 1/i)**i, 2))
#     sum += ((1 + 1/i)**i)
# print(list)
# print(sum)

# задача 4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
# print('Введите число: ', end = "")
# n = int(input())
# list = []
# path = 'file.txt'
# multpl = 1
# import random
# for i in range(1, n+1):
#     list.append(random.randint(-n, n))
# print(list)
# data = open(path, 'r')
# for line in data:
#     multpl *= list[int(data[line])]  #не удается корректно конвертировать данные из файла в int
# data.close()
# print(multpl)

# задача 5
# Реализуйте алгоритм перемешивания списка
print('Введите число: ', end = "")
n = int(input())
list = []
import random
for i in range(1, n+1):
    list.append(random.randint(-n, n))
print(list)
for i in list:
    rnd = random.randint(i, n-1)
    temp = list[i]
    list[i] = list[rnd]
    list[rnd] = temp
print(list)