"""Defining a class function."""
def inherits_from(obj, a_class):
    """Examining if the object is an inherited instance of a_class.
    obj(any): the checking obj.
    a_class(type): obj to be match to this class
    
    Returns:
        True - if object is an inherited instance of a_class.
        otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    #if issubclass(type(obj), a_class) and type(obj) == a_class:
    return False