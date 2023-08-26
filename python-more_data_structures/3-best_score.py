def best_score(a_dictionary):
    biggest_int = None
    biggest_value = float('-inf')

    for int  , value in a_dictionary.items():
        if value > biggest_value:
            biggest_int = int
            biggest_value = value
    return biggest_int



    #for score in a_dictionary:
        #biggest_integer.append(score)
    #return biggest_integer 