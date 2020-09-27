#class_pupils = input('введите имена учеников через запятую:\n')
class_pupils = 'АРина'
correct_result = ['Арина']

_result = class_pupils.strip(',')
result = []
for item in _result:
    result.append(item.strip().title())

print(result)
assert result == correct_result, 'алгоритм реализован неверно'
