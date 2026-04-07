class CodeBuilder:
    def __init__(self, class_name):
        self.class_name = class_name
        self.fields = []

    def add_field(self, name, value):
        self.fields.append((name, value))
        return self

    def __str__(self):
        res = [f"class {self.class_name}:"]

        res.append("  def __init__(self):")

        if not self.fields:
            res.append("    pass")
        else:
            for name, value in self.fields:
                res.append(f"    self.{name} = {value}")

        return "\n".join(res)


if __name__ == '__main__':
    cb = CodeBuilder('Person') \
        .add_field('name', '""') \
        .add_field('age', '0')

    print(cb)