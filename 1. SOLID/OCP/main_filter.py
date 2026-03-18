from Product_filter import *
from SizeSpecification import *
from ColorSpecification import *
from AndSpecification import *
from BetterFilter import *
from Color import *

if __name__ == "__main__":

   apple = Product("Apple", Color.GREEN, Size.SMALL)
   tree = Product("Tree", Color.GREEN, Size.LARGE)
   house = Product("House", Color.BLUE, Size.LARGE)

   products = [apple, tree, house]

   bf = BetterFilter()

   print("Green products:")
   green = ColorSpecification(Color.GREEN)
   for p in bf.filter(products, green):
       print(f" - {p.name} is green")

   print("Large products:")
   large = SizeSpecification(Size.LARGE)
   for p in bf.filter(products, large):
       print(f" - {p.name} is large")

   print("Large blue items:")
   large_blue = large and ColorSpecification(Color.BLUE)
   for p in bf.filter(products, large_blue):
       print(f" - {p.name} is large and blue")