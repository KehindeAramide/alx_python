def safe_print_division(a, b):
    try:
        #result = a / b
        print("{:d} / {:d} = {}".format(a, b))
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        #return result
    

#safe_print_division(12, 2)
#safe_print_division(12, 0)
#safe_print_division(12, 6)