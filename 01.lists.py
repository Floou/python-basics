import sys

my_list = [12, '16', 95.32, 55, True]
print(my_list, type(my_list), id(my_list), sys.getsizeof(my_list))

my_list = 12
print(my_list, type(my_list), id(my_list), sys.getsizeof(my_list))

my_list = 12.5
print(my_list, type(my_list), id(my_list), sys.getsizeof(my_list))

my_list = '12.5'
print(my_list, type(my_list), id(my_list), sys.getsizeof(my_list))
