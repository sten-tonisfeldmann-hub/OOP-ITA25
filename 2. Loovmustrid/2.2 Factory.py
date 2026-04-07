class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    def __init__(self):
        self.current_id = 0

    def create_person(self, name):
        new_person = Person(self.current_id, name)
        self.current_id += 1
        return new_person

if __name__ == '__main__':
    factory = PersonFactory()

    p1 = factory.create_person("Anna")
    p2 = factory.create_person("Mark")
    p3 = factory.create_person("Johannes")

    print(f"{p1.id} {p1.name}")
    print(f"{p2.id} {p2.name}")
    print(f"{p3.id} {p3.name}")