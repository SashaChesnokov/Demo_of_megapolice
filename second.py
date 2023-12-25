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

def main():
    student_data_from_csv = read_csv('student_new.csv')
    print(student_data_from_csv)

main()






