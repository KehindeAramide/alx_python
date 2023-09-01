#def multiply_list_map(my_list=[], number=0):
    #return (list(map((lambda i: i * number), my_list)))
def multiply_list_map(my_list=[], number=0):
    multiply = (lambda x: x * number)
    return (list(map(multiply, my_list)))