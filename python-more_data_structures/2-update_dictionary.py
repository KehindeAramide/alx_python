def print_sorted_dictionary(a_dictionary):
    list_arr = list(a_dictionary.keys())
    list_arr.sort()
    for i in list_arr:
        print("{}: {}".format(i, a_dictionary.get(i)))
