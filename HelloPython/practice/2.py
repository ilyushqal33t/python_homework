# Данная программа должна вывести n рядов, заполненных знаком ‘*’ определенным образом. А именно: в первом ряду должно быть n «звездочек», в втором n-1, и так далее. А в последнем ряду таким образом будет одна «звездочка». Причем убывать эти «звездочки» должны справа налево. Число n вводится пользователем.
# n = abs(int(input('Введите число ')))
# text = '*'*n
# for x in range(n):
#     print(text[0:len(text)- 1:])

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)
a, b, c = 1, 2, 3
# a: 1 b: 2 c: 3
print('a: {} b: {} c: {}'.format(a, b, c))

