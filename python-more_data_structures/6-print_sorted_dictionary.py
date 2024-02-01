#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # create list with keys of dictionary sorted
    sorted_keys = sorted(a_dictionary.keys())
    # loop on each key
    for key in sorted_keys:
        # get the value associated with each key and assigned it at value
        value = a_dictionary[key]
        # print key & value associated, replaced at each iteration
        print(f"{key}: {value}")
