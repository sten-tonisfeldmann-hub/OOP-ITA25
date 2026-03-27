from abc import ABC, abstractmethod

class Shape(ABC):
    """Class named Shape."""

    @abstractmethod
    def area(self):
        """Every shape should be able to calculate their area."""
        pass

    @abstractmethod
    def __str__(self):
        """All shapes should be represented as strings."""
        pass