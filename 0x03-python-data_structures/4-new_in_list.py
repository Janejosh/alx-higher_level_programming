#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = my_list[:]
    if idx < 0:
        return i
    if idx > len(my_list) - 1:
        return i
    i[idx] = element
    return i
