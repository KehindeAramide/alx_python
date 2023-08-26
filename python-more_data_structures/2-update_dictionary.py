def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    keys = sorted(a_dictionary.keys())
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))