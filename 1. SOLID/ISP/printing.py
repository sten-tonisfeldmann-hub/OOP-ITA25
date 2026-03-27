from abc import ABC, abstractmethod
class Printer(ABC):
    """Class for printing."""
    @abstractmethod
    def print_document(self, document):
        pass