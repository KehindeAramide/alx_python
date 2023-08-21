def safe_print_division(a, b):
    try:
        result = a / b
    except:
        result = None
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
    else:
        print("inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
    
