"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name, id):
        """Class named Student."""
        self.__name = name
        self.__id = id
        self.__status = "Active"

    def get_id(self):
        """get_id."""
        return self.__id

    def get_name(self):
        """get_name."""
        return self.__name

    def get_status(self):
        """get_status."""
        return self.__status

    def set_name(self, name):
        """set_name."""
        self.__name = name

    def set_status(self, status):
        """set_status."""
        status_list = ["Active", "Expelled", "Finished", "Inactive"]
        if status in status_list:
            self.__status = status


if __name__ == '__main__':
    student = Student("Mallu", "3")
    print(student.get_id())
    print(student.get_name())
    id_student = student.get_id()
    student_name = student.get_name()
    status_student = student.get_status()
    student_set_name = student.set_name("")