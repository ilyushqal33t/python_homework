def input_contact():
    list = ['id', 'имя', 'фамилию', 'номер телефона', 'комментарий']
    str =''
    for i in list:
        print(f'Введите {i}')
        str += input() + (';' if i != 'комментарий' else '')
    with open('directory.csv', 'a', encoding = 'UTF-8') as data:
        data.write(f'{str}\n')