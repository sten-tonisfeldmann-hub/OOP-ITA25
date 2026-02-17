"""Course class with name and grades."""


class Course:
    """Course class with name and grades."""

    def __init__(self, name: str):
        """Course class."""
        self.name = name
        self.courses = []
        self.grades = []

    def add_grades(self, student, grade: int):
        """Add grades to the course."""
        self.grades.append((student, grade))

    def get_grades(self) -> list:
        """Get the grades of the course."""
        return self.grades

    def get_average_grade(self) -> float:
        """Get the average grade of the course."""
        if len(self.grades) == 0:
            return -1
        else:
            return sum(grade for _, grade in self.grades) / len(self.grades)

    def __repr__(self):
        """Represetation for Course."""
        return self.name