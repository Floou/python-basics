# 1
student_marks = []
while True:
    mark = input('Введите оценку студента:\n')
    if mark:
        student_marks.append(int(mark))
        if int(mark) > 5:
            print('Введите оценку от 1 до 5')
            student_marks.remove(int(mark))
    else:
       break
print('Оценки студентов', student_marks)
avg_mark = 0
for marks in student_marks:
    avg_mark += marks
avg_mark /= len(student_marks)
print('Средний балл',avg_mark)

# 2
