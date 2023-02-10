# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

# import pandas as pd

# df = pd.read_csv('E:/study/Python/HelloPython/california_housing_test.csv')
# print(df)
# df[(df['population'] < 500)]['median_house_value'].mean()

# Задача 42: Узнать какая максимальная households в зоне минимального значения population

# df['population'].min()
# df[df['population']==5.0]['households'].max()

#39 задача f(x) = -12x^4 - 18x^3+5x^2 + 10x - 30

# Определить корни

# Найти интервалы, на которых функция возрастает

# Найти интервалы, на которых функция убывает

# Построить график

# Вычислить вершину

# Определить промежутки, на котором f > 0

# Определить промежутки, на котором f < 0

# import math
# from sympy import*
# from sympy.plotting import plot

# x = Symbol('x')
# fx = -12*x**4 - 18*x**3+5*x**2 + 10*x - 30
# sqrt_1, sqrt_2 = solve(fx)
# print(sqrt_1, sqrt_2)       #корни 
# p = plot(fx, (x, -10, 10))  #график
# apex = solve(diff(fx))[0]
# print(apex)                 #вершина
# solve(diff(fx)>0)           #интервал возрастания 
# solve(diff(fx)<0)           #интервал убывания
# solve(fx > 0)               #f > 0
# solve(fx < 0)               #f < 0