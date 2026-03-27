from relationship import *

class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        children = []
        for relation in self.relations:
            if relation[0].name == name and relation[1] == Relationship.PARENT:
                children.append(relation[2].name)
        return children