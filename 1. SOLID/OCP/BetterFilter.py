class BetterFilter:
    """Better filter"""
    def filter(self, products, spec):
        filter_products = []
        for product in products:
            if spec.is_satisfied(product):
                filter_products.append(product)

        return filter_products


