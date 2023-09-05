"""Defining a class function."""
def is_kind_of_class(obj, a_class):
    """Examining if the object is exactly an instance of the specified class.
    obj(any): the checking obj.
    a_class(type): obj to be match to this class
    
    Returns:
        True - if object is exactly an instance.
        otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    if type(obj) != a_class:
        return False