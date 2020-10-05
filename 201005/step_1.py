import students_stat

students_log = students_stat.parse_marks('students_log.txt')
students_log_as_dict = students_stat.parse_marks_as_dict('students_log.txt')
students_stat.save_marks('students_log.csv', students_log)
students_stat.save_marks_as_dict('students_log.json', students_log_as_dict)