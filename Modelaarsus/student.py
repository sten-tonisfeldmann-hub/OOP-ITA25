"""Student class with student name and grades."""


class Student:
    """Student class with student name and grades."""

    def __init__(self, name):
        """Initialize the Student class."""
        self.name = name
        self.grades = []
        self.id = None

    def set_id(self, id):
        """Set the Student ID."""
        if self.id is None:
            self.id = id
        else:
            return

    def get_id(self):
        """Get the Student ID."""
        return self.id

    def add_grade(self, course, grade: int):
        """Add a Grade to the Student."""
        self.grades.append((course, grade))

    def get_grades(self) -> list:
        """Get the Student Grades."""
        return self.grades

    def get_average_grade(self):
        """Get the Average Grade."""
        if len(self.grades) == 0:
            return -1
        else:
            return sum(grade for _, grade in self.grades) / len(self.grades)

    def __repr__(self):
        """School class anfwkajfkawbfba."""
        return self.name