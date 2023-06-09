#!/user/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        if i == idx:
            return my_list[i]
    else:
        return None
