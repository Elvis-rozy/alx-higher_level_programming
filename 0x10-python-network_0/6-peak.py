#!/usr/bin/python3
"""
finds a peak(highest) in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds the peak in the array
    """
    if bool(list_of_integers) is False:
        return None
    i = len(list_of_integers) - 1
    while i > 1:
        j = 0
        while j < i:
            if list_of_integers[j] > list_of_integers[j + 1]:
                temp = list_of_integers[j]
                list_of_integers[j] = list_of_integers[j + 1]
                list_of_integers[j + 1] = temp
            j += 1
        i -= 1
    return list_of_integers[-1]

