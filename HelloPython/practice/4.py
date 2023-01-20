# 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# n = input('Введите числа через пробел: ').split()
# n_list=list(map(int,n))
# print(n_list)
# print(max(n_list), min(n_list))



# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# import math
# a_ = int(input('a= '))
# b_ = int(input('b= '))
# c_ = int(input('c= '))
# d_= (math.pow(b_,2))-4*a_*c_
# print(d_)
# if d_ == 0:
#     print('Дискриминант равен 0')
#     x1_ = -b_/(2*a_)
#     print(f'Х1= {x1_}')
# elif d_ < 0:
#     print('Корней нет')
# else:
#     x1_ = (-b_ + math.sqrt(d_))/(2*a_)
#     x2_ = (-b_ - math.sqrt(d_))/(2*a_)
#     print(f'Х1= {x1_}, X2= {x2_}')

# 29. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел

# a = int(input())
# b = int(input())

# for i in range(max(a,b),a*b+1,max(a,b)):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break