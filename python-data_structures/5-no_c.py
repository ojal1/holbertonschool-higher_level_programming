#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    while 'C' in my_list:
        my_list.remove('C')
    while 'c' in my_list:
        my_list.remove('c')
    new_string = ''.join(my_list)
    return new_string
