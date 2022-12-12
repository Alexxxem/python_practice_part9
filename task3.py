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


def get_student(students):
    course = int(input('Enter course number: '))
    sorted_students = sorted(students)
    result = []
    for _ in sorted_students:
        if _[4] == course:
            result.append(_)
    return result


def get_youngest_and_oldest_students(students):
    maximum = 2022
    minimum = 1900
    youngest_student = ()
    oldest_student = ()
    result = []
    for _ in students:
        if _[3] > minimum:
            youngest_student = _
            minimum = _[3]
        if _[3] < maximum:
            oldest_student = _
            maximum = _[3]

    result.append(youngest_student)
    result.append(oldest_student)
    return result



students = [
    ('Иванов', 'Сергей', 'Дмитриевич', 2003, 2, '431-1'),
    ('Петров', 'Кирилл', 'Олегович', 2002, 3, '430-2'),
    ('Сергеева', 'Елизавета', 'Викторовна', 2005, 3, '430-2'),
    ('Кузнецов', 'Валерий', 'Андреевич', 2002, 3, '430-1'),
    ('Соколова', 'Виктория', 'Сергеевна', 2003, 2, '431-1'),
    ('Попов', 'Виктор', 'Александрович', 2004, 1, '432-1'),
]


# course_students = get_student(students)
# for student in course_students:
#     print(student)

youngest_and_oldest = get_youngest_and_oldest_students(students)
for _ in youngest_and_oldest:
    print(_)

