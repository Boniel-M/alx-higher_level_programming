#!/usr/bin/python3
def uniq_add(my_list=[]):

    uniq_int = set()

    for element in my_list:
        uniq_int.add(element)

    sum_uniq = sum(uniq_int)
    return sum_uniq
