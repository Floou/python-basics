#student_marks = []
#while True:
#    mark = input('введите оценку студента:\n')
#    if mark:
#        student_marks.append(mark)
#    else:
#        break
#
#print('ввод завершен')
#print(student_marks)

mock_student_mark = ['5', '4', '3', '2', '5']
student_marks = mock_student_mark

i = 0
avg_mark = 0
while i < len(student_marks) :
    #print(type(avg_mark), type(student_marks[i]))
    avg_mark +=int(student_marks[i])
    i += i + 1
avg_mark /= len(student_marks)
print('средний балл',avg_mark)
