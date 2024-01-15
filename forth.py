import csv

def read_csv(file_path):
    '''
    Чтение данных в CSV формате из файла.
    
    Args:
        file_path (str): Путь к файлу.
    Returns:
        student_data (list of dict): Список словарей с данными студентов.
    '''

    student_data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_data.append(row)

    return student_data

def generate_login(student_data):
    for student in student_data:
        new_login = student['surname'] + '_' + student['name'][0] + student['patronymic'][0]
        student['login'] = new_login
    return student_data

for i in generate_login(read_csv('student.csv')):
    print(i)