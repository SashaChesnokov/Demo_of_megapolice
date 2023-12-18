import csv

student_data = [
    {"name": "Андрей", "surname": "Попов", "grade": 5, "project_id": "1"},
    {"name": "Степан", "surname": "Васильев", "grade": None, "project_id": "2"},
    {"name": "Владимир", "surname": "Хадаров", "grade": 4, "project_id": "3"}
]

def calculate_average_grade(grades_list):
    '''
    Вычисление средней оценки из списка оценок.

    Args:
    grades_list (list): Список оценок.

    Returns:
    float: Средняя оценка.
    '''

    valid_grades = [grade for grade in grades_list if grade is not None]
    
    return round(sum(valid_grades)/len(valid_grades), 3) if valid_grades else 0

def process_student_data(student_data):
    '''
    Обработка данных студентов
    
    Args:
    student_data (list of dict): Список словарей с данными студентов.

    Returns:
    list of dict: Обработанный список с данными студентов.
    '''

    grades = [student['grade'] for student in student_data]

    average_grade = calculate_average_grade(grades)

    for student in student_data:
        if student['grade'] is None:
            student['grade'] = average_grade
    
    return student_data

