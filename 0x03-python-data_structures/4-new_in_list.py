#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    #check if the is index(idx) is negative or out of bound

    if idx < 0 or idx >= len(my_list):
        return my_list[:] #returns the original list if condition above is met

    new_list = my_list[:] #Assigns a copy of the list to the newlist
    
    #Relaces the elemnet with a new element in the new list at the specified index
    new_list[idx] = element
    return new_list 
