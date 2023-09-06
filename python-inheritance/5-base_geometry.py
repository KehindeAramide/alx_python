"""
Define an empty class named BaseGeometry
"""
class BaseGeometry:
    '''
    this represents BaseGeometry
    '''
    
    def __init_subclass__(cls):
        bg = BaseGeometry()
        """Creating an instance for BaseGeometry"""
        attributes_and_methods = dir(bg)
        """Getting attributes and methods of instance"""
        class_attributes_and_methods = dir(BaseGeometry)

        pass
    
    def __dir__(self):
        """ Get the default list of attributes and methods"""
        default_attrs = super().__dir__()
    

        """Exclude '__init_subclass__' if it exists in the list"""
        if '__init_subclass__' in default_attrs:
            default_attrs.remove('__init_subclass__')

        return default_attrs
    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
