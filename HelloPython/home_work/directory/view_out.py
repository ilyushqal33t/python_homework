def print_directory():
    print('Введите "all", чтобы посмотреть весь справочник, введите id, чтобы посмотреть данные пользователя: ')
    list = ['id','имя','фамилия','телефон','комментарий']
    id = input()
    with open('directory.csv', 'r', encoding = 'UTF-8') as data:
        if id == 'all':
            for line in data:
                print(line)
        else:
            for line in data:
                if id in line:
                    for i,v in enumerate(line.split(';')):
                        print(f'{list[i]}: {v}')
                    break