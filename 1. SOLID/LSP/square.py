from shape import Shape

class Square(Shape):
    """Class named square."""
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def area(self):
        return self._size ** 2

    def __str__(self):
        return f"Square (Side: {self._size})"