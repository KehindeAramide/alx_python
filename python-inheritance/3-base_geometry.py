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
        # Get the default list of attributes and methods
        default_attrs = super().__dir__()
        default

        # Exclude '__init_subclass__' if it exists in the list
        if '__init_subclass__' in default_attrs:
            default_attrs.remove('__init_subclass__')

        return default_attrs