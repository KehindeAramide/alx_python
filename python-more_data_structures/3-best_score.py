def best_score(a_dictionary):
    biggest_score = None
    biggest_value = float('-inf')

    for int  , value in a_dictionary.items():
        if value > biggest_value:
            biggest_value = value
    return biggest_score
