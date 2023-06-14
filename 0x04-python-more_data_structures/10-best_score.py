#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    
    best_key = None
    best_score = float('-inf')

    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > best_score:
            best_key = key
            best_score = value

    return best_key
