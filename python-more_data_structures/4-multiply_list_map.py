def multiply_list_map(my_list=[], number=0):
    multiply = (lambda x: x * number)
    return (list(map(multiply, my_list)))