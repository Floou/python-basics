mock_student_mark = [5, 4, 3, 2, 5]

print(mock_student_mark)
mock_student_mark.append(5)
print(mock_student_mark)
#print(mock_student_mark.index(5, 1))
#print(mock_student_mark.index(5, 5))
#print(mock_student_mark.index(5, 1, 5))

#print('5 count', mock_student_mark.count(5))
#print('2 count', mock_student_mark.count(2))
#print(mock_student_mark.count(15))

num = 5
if mock_student_mark.count(num):
    print(num, 'found', mock_student_mark.index(num), 'times, first index', mock_student_mark.index(num))
else:
    print(num, 'not found')