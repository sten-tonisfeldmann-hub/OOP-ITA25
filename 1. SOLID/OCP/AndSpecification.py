class AndSpecification:
    """Product filter class"""
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def filter_by_size_and_color(self, product):
        """Filter product by size and color"""
        return self.size == product.size and self.color == product.color