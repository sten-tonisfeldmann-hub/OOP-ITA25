from person import Person
from relationships import Relationships
from research import Research


if __name__ == "__main__":
    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Matt')

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    Research(relationships)