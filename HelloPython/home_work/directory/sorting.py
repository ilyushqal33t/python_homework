def sort():
    with open('directory.csv', 'r+', encoding = 'UTF-8') as data:
        res_data = sorted(data, key = lambda line: int(line.split(';')[0]))
        data.seek(0)
        for i in res_data:
            data.write(i)