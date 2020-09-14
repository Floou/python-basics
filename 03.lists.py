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
#lesson_dates_and_marks = [
#    ['19.03.05', 5],
#    ['19.03.08', 4],
#    ['19.03.10', 3],
#    ['19.03.19', 2],
#    ['19.03.21', 5]
#]
#for record in lesson_dates_and_marks:
#    lesson_dates, mark = record
#    print(lesson_dates, 'оценка', mark)
for lesson_dates, mark,mark2 in zip(lesson_dates, student_marks, student_2_marks):
    print(lesson_dates, 'оценка', mark, mark2)

#i = 0
#while i < len(student_marks):
#    print(lesson_dates[i], 'оценка', student_marks[i])
#    i += 1  # i = 1

#for item in student_marks:
#     print('оценка', item)

#for item in enumerate(student_marks):
#     print('оценки', item)

#for i, item in enumerate(student_marks):
#      print('оценка', i, item)
