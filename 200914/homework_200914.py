# 1
#student_marks = []
#while True:
#    mark = input('Введите оценку студента:\n')
#    if mark:
#        student_marks.append(int(mark))
#        if int(mark) > 5:
#            print('Введите оценку от 1 до 5')
#            student_marks.remove(int(mark))
#    else:
#       break
#print('Оценки студентов', student_marks)
#avg_mark = 0
#for marks in student_marks:
#    avg_mark += marks
#avg_mark /= len(student_marks)
#print('Средний балл',avg_mark)

# 2
lesson_dates = [
    '19.03.05',
    '19.03.08',
    '19.03.10',
    '19.03.19',
    '19.03.21'
]
student_marks = [
    5,
    4,
    3,
    2,
    5
]
student_2_marks = [
    5,
    4,
    3,
    2,
    5
]
for lesson_date, mark, mark_2 in zip(lesson_dates, student_marks, student_2_marks):  # ['19.05.15', 5, 4]
    # print(lesson_date, 'оценка', 'студента 1', mark, ', студента 2', mark_2)
    print(lesson_date)

curren_date = input('введите дату:\n')
if not lesson_dates.count(curren_date):
    date_index = lesson_dates.index(curren_date)
    print('оценки студентов за', lesson_dates[date_index], ':', student_marks[date_index], student_2_marks[date_index])
else:
    print('ошибка даты:', curren_date)
#try:
#    date_index = lesson_dates.index(curren_date)
#    print(student_marks[date_index], student_2_marks[date_index])
#except Exception as e:
#    print('ошибка', e)
#date_index = 3
