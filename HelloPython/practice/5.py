#lambda, filter, map, zip, enumerate, list comprehension

# a = []
# for i in range(1,9):
#     a.append(i)
# print(a)
#list comprehension
# a = [i*i for i in range(1,9)]
# print(a)
#enumerate
# a = [1, 4, 9, 16, 25, 36, 49, 64]
# for indx,value in enumerate(a):
#     print(indx,value)
#zip
# num=[1,2,3,4,5,6,7]
# months = ["июнь", "июль","июль2","июль3","июль4","июль5"]
#
# a = list(zip(num,months))
# print(a)
#lambda
# def summ(a,b):

#      return a+b
# print(summ(3,5))

# summ = lambda a,b: a+b if a>5 else 0
# print(summ(2,5))

#map
# a = [i for i in range(12)]
# print(a)
# a = list(map(lambda x:x+10 if x >6 else x + 0,a))
# print(a)
#filter
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# def chek_num(x):
#     if x%2==0:
#         return True
# a_chet = list(filter(lambda  x:True if x%2 == 0 else False,a))
# print(a_chet)

# ----------------------------------------------------------
# lst_1 = [1, 2, 3, 5, 7, 8, 9, 10]
# lst_2 = [1, 2, 4, 8, 9]


# a = list(filter((lambda x: x in lst_1), lst_2))
# print(a)

# -------------------------------------

# str = 'фыыо лыбш, уальуц а абв фбвб фыфыфф цабвыц'

# lst = str.split()

# lst_2 = ' '.join(list(filter(lambda x: 'абв' not in x, lst)))
# print(lst_2)

# for i, sym in enumerate(str):
#     if sym == ' ':
#         print(i, sym)

# ---------------------------------------

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i, v in enumerate(a):
#     print(i, v)
#     v[i] = 0
# print(a)

# ---------------------------------------------

# from random import randint

# id = [randint(1, 100) for _ in range(5)]
# names = ['ivanov', 'petrov', 'sidorov', 'kuznecov', 'potapov']

# lst = list(zip(id, names))
# print(lst)

# lst_odd = [elem[1] for elem in lst if elem[0] % 2 != 0]
# print(lst_odd)