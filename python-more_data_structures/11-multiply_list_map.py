#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = []
    new_list = list(map(lambda value: value * number, my_list))
    return (new_list)
