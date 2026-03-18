from enum import Enum


"""A product filter"""

class Product:
    """Product class"""
    def __init__(self, name, color, size):
        """Product constructor"""
        self.name = name
        self.color = color
        self.size = size


class Size(Enum):
    """Size class"""
    SMALL = 1
    MEDIUM = 2
    LARGE = 3




