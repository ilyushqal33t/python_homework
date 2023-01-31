def input_student(dict, subjects):
    student = input('введите имя и фамилию ученика: ')
    dict[student] = {}
    for i in subjects:
        dict[student][i] = []
    


def input_subjetc(subjects, dict):
    subj = input('введите название предмета: ')
    subjects.append(subj)
    for i in dict:
        dict[i][subj] = []

def input_marks(dict):
    st_keys = list(dict.keys())
    print('Введите номер ученика из списка ниже')
    for indx, key in enumerate(st_keys):
        print(f'{indx+1}){key}')
    stdnt = int(input())
    sub_keys = list(dict[st_keys[stdnt-1]].keys())
    print('Введите номер предмета из списка ниже')
    for indx, key in enumerate(sub_keys):
        print(f'{indx+1}){key}')
    sbjct = int(input())
    mark = input('Введите оценку: ')
    dict[st_keys[stdnt-1]][sub_keys[sbjct-1]].append(mark)

