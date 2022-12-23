# list_num = [3, 4, 1, 2, 'asd', '132']
# find = int(input())
# for i in range(len(list_num)):
#     if list_num[i] == find:
#         print(i)
#         break
# else:
#     print('Такого числа нет')

# import datetime
# def random_int(num):
#     rand = datetime.datetime.now().microsecond/10**6
#     return int((num+1)*rand)

# n = int(input())
# print(random_int(n))

# 21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# find = "qwe"
# count = 0
# for i in range(len(list)):
#     if list[i] == find:
#         count += 1
#     if count == 2:
#         print(i)
#         break
# else:
#     print(-1)
