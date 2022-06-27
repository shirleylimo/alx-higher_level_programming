#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height
            Args:
                width(int): width of the rectangle
                Length(int): Length of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter
           Returns: width as a private att
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """ sets value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        self.__width = value
        
    @property
    def height(self):
        """ height getter
            Returns: height of rec
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter
            Args:
                value: integer of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        self.__height = value
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """ area of a rec
            returns: area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter of rec
            returns: perimeter of rec
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))
