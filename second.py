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

def insertion_sort(student_data, key):
    '''
    Алгоритм сортировки вставками.
    
    Args:
        student_data (list of dict): Список словарей с данными студентов.
        key (str): Ключ, по которому будет проводиться сортировка
    Returns:
        student_data (list of dict): Отсортированный по возрастанию список словарей с данными студентов.
    '''
    
    for i in range(1, len(student_data)):
        curent_value = student_data[i]
        position = i

        while position > 0 and student_data[position-1][key] > curent_value[key]:
            student_data[position] = student_data[position-1]
            position -= 1
        
        student_data[position] = curent_value
        
    return student_data[::-1]

def print_top_students(student_data, count_of_students):
    '''
    Алгоритм сортировки вставками.
    
    Args:
        student_data (list of dict): Список словарей с данными студентов.
        count_of_students (int): Количество студентов, которых нужно вывести
    '''

    place = 1
    for student in student_data[:count_of_students]:
        print(f"{place} место {student['name'][0]}.{student['surname']}")
        place += 1





def main():
    student_data_from_csv = read_csv('student_new.csv')
    sorted_student_data = insertion_sort(student_data_from_csv, 'grade')
    print_top_students(sorted_student_data, 3)

main()






