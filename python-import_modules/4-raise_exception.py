def raise_exception():
    a = str
    b = int
    result = a + b
    return result
# Call the function to see the exception
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
