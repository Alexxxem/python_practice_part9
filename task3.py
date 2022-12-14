# 3. Деканат.
# Дано: список студентов: каждый элемент списка содержит фамилию,
# имя, отчество, год рождения, курс, номер группы, оценки по пяти предметам.
#
# Задание: реализуйте сл. функции:
#
# 1) возвращает список студентов по курсу, причем студенты одного курса располагались в алфавитном порядке;
# 2) находит средний балл каждой группы по каждому предмету;
# 3) определяет самого старшего студента и самого младшего студента.
# 4) возвращает словарь, где для каждой группы определен лучший с точки зрения успеваемости студент.


def get_students(students):
    course = int(input('Enter course number: '))
    result = [_ for _ in students if _[4] == course]
    sorted_students = sorted(result)
    return sorted_students


def get_group_average_mark_in_subject():
    pass


def get_youngest_and_oldest_students(students):
    max_birth_year = min_birth_year = students[0][3]
    youngest_student = ()
    oldest_student = ()
    result = []

    for _ in students:
        if _[3] > min_birth_year:
            youngest_student = _
            min_birth_year = _[3]
        if _[3] < max_birth_year:
            oldest_student = _
            max_birth_year = _[3]

    result.append(youngest_student)
    result.append(oldest_student)
    return result


def get_best_student_of_group(students):
    best_students = {}

    for _ in students:
        group = _[5]
        marks = _[6:]
        student = _[:3]
        if group in best_students.keys():
            if sum(best_students[group][1]) < sum(marks):
                best_students[group] = [student, marks]
        else:
            best_students[group] = [student, marks]
    return best_students


if __name__ == '__main__':

    students = [
        ('Иванов', 'Сергей', 'Дмитриевич', 2003, 2, '431-1', 4, 5, 4, 4, 4),
        ('Петров', 'Кирилл', 'Олегович', 2002, 3, '430-2', 4, 5, 3, 4, 3),
        ('Сергеева', 'Елизавета', 'Викторовна', 2005, 3, '430-2', 5, 5, 5, 4, 5),
        ('Кузнецов', 'Валерий', 'Андреевич', 2002, 3, '430-1', 5, 5, 5, 5, 5),
        ('Соколова', 'Виктория', 'Сергеевна', 2003, 2, '431-1', 4, 5, 5, 4, 5),
        ('Попов', 'Виктор', 'Александрович', 2004, 1, '432-1', 3, 4, 3, 4, 5),
    ]

    while True:
        answer = int(input('Select the number:\n'
                           '1. Get the list of students from the course\n'
                           '2. Get an average mark of the group in a subject\n'
                           '3. Get the youngest and oldest student\n'
                           '4. Get the best student of each group\n'))
        if answer == 1:
            course_students = get_students(students)
            print('List of students from the course: ')
            for _ in course_students:
                print(_)
            break
        if answer == 2:
            break
        if answer == 3:
            youngest_and_oldest = get_youngest_and_oldest_students(students)
            print('Youngest and oldest student: ')
            for _ in youngest_and_oldest:
                print(_)
            break
        if answer == 4:
            best_students = get_best_student_of_group(students)
            for group, student in best_students.items():
                print(group, student)
            break
