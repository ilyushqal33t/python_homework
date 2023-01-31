def print_students(dict):
    for i in dict.keys():
        print(i)

def print_marks_student(dict):
    st_keys = list(dict.keys())
    print('Введите номер ученика из списка ниже')
    for indx, key in enumerate(st_keys):
        print(f'{indx+1}){key}')
    student = int(input())
    for sub, marks in dict[st_keys[student-1]].items():
        print(f'{sub}: {marks}')
