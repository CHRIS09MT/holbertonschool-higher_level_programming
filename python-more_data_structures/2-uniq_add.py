#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = [i + 1 for i in my_list if my_list.count(i) == 1]
    return sum(result)
