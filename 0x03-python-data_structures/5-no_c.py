#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        i = my_string.translate({ord("c"): None})
        j = i.translate({ord("C"): None})
        return j
    return my_string
