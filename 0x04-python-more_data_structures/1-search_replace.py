#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element by another in a new list.
    :param my_list: The initial list
    :param search: The element to replace in the list
    :param replace: The new element
    :return: A new list with all occurrences of search replaced by replace
    """
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
