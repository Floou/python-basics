lesson_dates = [
    '19.05.15',
    '19.05.17',
    '19.05.18',
    '19.05.19',
    '19.05.22',
]
student_marks = [
    5,
    4,
    3,
    2,
    5
]
student_2_marks = [
    4,
    3,
    5,
    5,
    4
]

for lesson_dates, mark, mark_2 in zip(lesson_dates, student_marks, student_2_marks):
    print(lesson_dates, 'оценка', mark, mark_2)
date = input('Введите дату:\n')

if lesson_dates.count(date):
    date_index = lesson_dates.index(date)
    print('оценки студентов за ', lesson_dates[date_index], ':', student_marks[date_index], student_2_marks[date_index])
else:
    print('ошибка даты:', date)