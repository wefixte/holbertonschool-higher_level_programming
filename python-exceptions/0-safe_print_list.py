#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count_element = 0
        for index in range(x):
            print("{}".format(my_list[index]), end="")
            count_element += 1
        print()
        return count_element
    except IndexError:
        print()
        return count_element
