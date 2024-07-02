#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [0, 8, 9, 3, -2, 4]
idx = -9 
element = 200

new_list = replace_in_list(my_list, idx, element)
print(f'New List is {new_list}')
print(f'My List is {my_list}')
