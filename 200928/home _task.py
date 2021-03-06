with open('students_log.txt', 'r', encoding='utf-8') as f:
    for row in f.read().splitlines():
        last_name, first_name, patronymic, row_marks = row.split(maxsplit=3)
        patronymic = patronymic.strip(',')
        marks = []
        for mark in row_marks.split(','):
            marks.append(int(mark.strip()))
        avg_mark = sum(marks) / len(marks)
        print(last_name, first_name, patronymic, ':', marks, ', средний балл', avg_mark)
