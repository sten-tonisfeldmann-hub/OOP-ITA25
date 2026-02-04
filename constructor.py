"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass



class Person:
    """Represent person with firstname, lastname and age."""
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = ""
    pass


class Student:
    """Represent student with firstname, lastname and age."""
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    pass


if __name__ == '__main__':
    # empty usage
    empty = Empty()
    # 3 x person usage
    person = Person()
    # 3 x student usage
    student = Student("Mallu", "kiisu", "3")
    pass
