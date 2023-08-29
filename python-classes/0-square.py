class Square:
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2

    #def __str__(self):
        #return f"Square with side length {self.__size}"