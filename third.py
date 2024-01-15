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

def find_student_by_project_id(student_data, project_id):
    '''
    Поиск ученика, который выполнил проект.
    Args:
        student_data (list of dict): Список словарей с данными студентов.
        project_id (int): ID проекта.
    Returns:
        student_information (str): Данные о студенте.
    '''

    for student in student_data:
        if int(student['project_id']) == project_id:
            return f"Проект № {project_id} делал: {student['name'][0]+'.'+student['surname']}. Он(а) получил(а) оценку - {student['grade']}"
    
    return 'Ничего не найдено.'

def main():
    student_data = read_csv('student.csv')
    command = input()
    while command != 'СТОП':
        project_id = int(command)
        print(find_student_by_project_id(student_data, project_id))
        command = input()

main()