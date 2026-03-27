class Rectangle:
    """class named rectangle"""
    def __init__(self, width, height):
        """Initialize width and height."""
        self._width = width
        self._height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self._width * self._height

    def __str__(self):
        """String representation of the rectangle."""
        return f"Width: {self._width}, Height: {self._height}"

    @property
    def width(self):
        """Define the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, new_width):
        """Set the width of the rectangle."""
        self._width = new_width

    @property
    def height(self):
        """Define the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, new_height):
        """Set new height of rectangle."""
        self._height = new_height

class Square(Rectangle):
    """class named square."""
    def __init__(self,size):
        """Define the super of the square."""
        super().__init__(size, size)

    def __str__(self):
        return f"Square with side: {self.width}"