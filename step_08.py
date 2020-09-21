# class_pupils = input('введите имена учеников через запятую:\n')
# Полина, Антон, Арсений, Евгений, Алексей, Тимур
# result = ['Полина', 'Антон', 'Арсений', 'Евгений', 'Алексей', 'Тимур']
# assertion
# TDD -> test driven development

# class_pupils = 'Полина, Антон, Арсений, Евгений, Алексей, Тимур'
# class_pupils = 'Полина, Антон, Арсений , Евгений,  Алексей, Тимур '
class_pupils = 'Полина,Антон, Арсений , Евгений,  Алексей, Тимур '
correct_result = ['Полина', 'Антон', 'Арсений', 'Евгений', 'Алексей', 'Тимур']

# result = class_pupils.split(',')
_result = class_pupils.split(',')  # raw
result = []
for item in _result:
    # print(item, '->', item.strip())
    result.append(item.strip())

print(result)
assert result == correct_result, 'алгоритм реализован неверно'
# assert True or False: True -> calm, False -> assertion ERROR

# if not result == correct_result:
#     raise AssertionError('алгоритм реализован неверно')

# class_pupils = input('введите имена учеников через запятую:\n')
class_pupils = 'Полина,Антон, Арсений , Евгений,  Алексей, Тимур '
correct_result = ['Полина', 'Антон', 'Арсений', 'Евгений', 'Алексей', 'Тимур']

# _result = class_pupils.split(',')
# result = []
# for item in _result:
#     result.append(item.strip())

# result = list(map(str.strip, class_pupils.split(',')))
# list comprehensions (bad idea - генераторы списков)
result = [item.strip() for item in class_pupils.split(',')]

# map
# [
#     'Полина', -> str.strip('Полина') -> 'Полина'
#     'Антон', -> ...
#     ' Арсений ', -> str.strip(' Арсений ') -> 'Арсений'
#     ' Евгений', -> ...
#     '  Алексей', ->
#     ' Тимур ' ->
# ]
print(result)
assert result == correct_result, 'алгоритм реализован неверно'
