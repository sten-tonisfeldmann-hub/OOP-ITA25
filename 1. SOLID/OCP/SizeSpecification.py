class SizeSpecification:
    """Size class"""
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, product):
        """Filter product by size"""
        return self.size == product.size