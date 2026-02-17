"""School class which stores information about courses and students."""

import random


class School:
    """School class which stores information about courses and students."""

    def __init__(self, name):
        """School class anfwkajfkawbfba."""
        self.name = name
        self.students = []
        self.courses = []

    def add_student(self, student):
        """School class anfwkajfkawbfba."""
        id = random.randint(0, 1000)
        for school_student in self.students:
            if school_student.id == id:
                id = random.randint(0, 1000)
        if student not in self.students:
            student.set_id(id)
            self.students.append(student)
        else:
            return

    def get_students(self):
        """School class anfwkajfkawbfba."""
        return self.students

    def add_course(self, course):
        """School class anfwkajfkawbfba."""
        if course not in self.courses:
            self.courses.append(course)
        else:
            return

    def get_courses(self):
        """School class anfwkajfkawbfba."""
        return self.courses

    def add_student_grade(self, student, course, grade: int):
        """School class anfwkajfkawbfba."""
        if course in self.courses and student in self.students:
            student.add_grade(course, grade)
            course.add_grades(student, grade)
        else:
            return

    def get_students_ordered_by_average_grade(self) -> list:
        """School class anfwkajfkawbfba."""
        ordered_students = sorted(self.students, key=lambda students: students.get_average_grade(), reverse=True)
        return ordered_students

    def __repr__(self):
        """School class anfwkajfkawbfba."""
        return self.name