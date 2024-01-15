import csv
from random import choice, shuffle
from string import ascii_uppercase, ascii_lowercase, digits

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

def generate_passwords(student_data):
    for student in student_data:
        new_password = [choice(ascii_lowercase), choice(ascii_uppercase), choice(digits)] + [choice(ascii_lowercase + ascii_uppercase + digits) for _ in range(5)]
        shuffle(new_password)
        new_password = ''.join(new_password)
        student['password'] = new_password
    return student_data

def save_to_csv(data, file_name):
    '''
    Запись данных в CSV формате в файл.
    
    Args:
    data (list of dict): Список словарей с данными студентов.
    file_name (str): Имя Файла для сохранения.
    '''

    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def main():
    student_data = read_csv('student.csv')
    student_data = generate_login(generate_passwords(student_data))
    save_to_csv(student_data, 'forth_task.csv')

main()