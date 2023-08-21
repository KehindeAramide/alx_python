def raise_exception_msg(message=""):
    raise NameError(message)

# Call the function to see the exception
try:
    raise_exception_msg()
except NameError as ne:
    print(ne)
