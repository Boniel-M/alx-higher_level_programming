#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced_item = []

    for element in my_list:
        if element == search:
            replaced_item.append(replace)
        else:
            replaced_item.append(element)
    return replaced_item
