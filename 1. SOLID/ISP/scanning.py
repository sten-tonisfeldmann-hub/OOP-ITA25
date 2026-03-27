from abc import ABC, abstractmethod
class Scanner(ABC):
    """Class for scanning."""
    @abstractmethod
    def scan_document(self, document):
        pass