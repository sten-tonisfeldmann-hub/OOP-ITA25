from rectangle import *
from square import *
from shape import *

if __name__ == "__main__":

    r = Rectangle(2, 3)
    s = Square(5)

    print(r)
    print(s)

    print(f"Rectangle area: {r.area}")
    print(f"Square area: {s.area}")