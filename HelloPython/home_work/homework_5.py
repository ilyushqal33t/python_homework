# 39(2) Создайте программу для игры в ""Крестики-нолики"".
# def sqr(list):
#     for i in range(3):
#         print(f'|{list[0 + i*3]}||{list[1 + i*3]}||{list[2 + i*3]}|')

# def check_position(list, player):
#     while True:
#         number = input(f'Ходит {player}: ')
#         if not(number in '123456789'):
#             print('Некорректное число')
#             continue
#         number = int(number)
#         if list[number-1] != str(number):
#             print('Клетка уже занята')
#             continue
#         list[number-1] = player
#         break
                    

# def check_win(list, space):
#     for i in list:
#         if (space[i[0] - 1] == space[i[1] - 1] == space[i[2] - 1]):
#             win_comb = [i[0], i[1], i[2]]
#             return win_comb
#     else:
#         return False

# win_pos = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]
# print('Вы играете крестиками, введите номер клетки (от 1 до 9) для хода')
# space = ['1','2','3','4','5','6','7','8','9']
# move = 0
# while True:
#     sqr(space)
#     if move % 2 == 0:
#         check_position(space, 'X')
#     else:
#         check_position(space, '0')
#     if move > 3:
#         winner = check_win(win_pos, space)
#         if winner:
#             sqr(space)
#             print(f'Комбинация {winner} победила!')
#             break
#     move +=1
#     if move > 8:
#         sqr(space)
#         print('Ничья')
#         break

# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# def compression(iterr):
#     count = 1
#     comp = ''
#     prev_char = ''

#     for i in iterr:
#         if i != prev_char:
#             if prev_char:
#                 comp += str(count) + prev_char
#             count = 1
#             prev_char = i
#         else:
#             count+=1
#     else:
#         comp += str(count) + prev_char
#         return comp

# def decompression(iterr):
#     decomp = ''
#     count = ''
#     for i in iterr:
#         if i.isdigit():
#             count += i
#         else:
#             decomp += i*int(count)
#             count =''
#     return decomp
# # Первоначальный вариант. Работает исправно, но только для букв((((

# def decompression(iterr):
#     decomp = ''
#     count = 0
#     digit = True
#     for i in iterr:
#         if digit:
#             count = int(i)
#             digit = False
#         else:
#             decomp += i*int(count)
#             digit = True
#     return decomp
# # Этот вариант украл из лекции))))

# def main():
#     comp = input('Введите строку для сжатия данных: ')
#     print(f'Ваша строка: {compression(comp)}')
#     decomp = input('Введите строку для восстановления данных: ')
#     print(f'Ваша строка: {decompression(decomp)}')

# main()