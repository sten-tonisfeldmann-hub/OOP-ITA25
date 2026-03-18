class ColorSpecification:
    def __init__(self, color):
        self.color = color

    """ColorSpecification class"""
    def is_satisfied(self, product):
        """Filter product by color"""
        return self.color == product.color