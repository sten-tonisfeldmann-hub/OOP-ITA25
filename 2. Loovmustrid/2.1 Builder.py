class CodeBuilder:
    def __init__(self, person):
        self.person = person
        self.fields = []

    def add_field(self, name, age):
        self.fields.append((age, name))
        return self

    def __str__(self):
        return f"His fields are {self.fields}."


if __name__ == '__main__':
    cb = CodeBuilder('Person') \
        .add_field('name', '""') \
        .add_field('age', '0')

    print(cb)