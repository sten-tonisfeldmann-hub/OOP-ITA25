from abc import ABC, abstractmethod
class Machine(ABC):
    """Class named machine."""

    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionPrinter(Machine):
    """Class named MFP."""
    def print(self, document):
        print(f"Printing document: {document}")

    def fax(self, document):
        print(f"Faxing document: {document}")

    def scan(self, document):
        print(f"Scanning document: {document}")
        return f"Scanned_{document}.pdf"

class OldFashionedPrinter(Machine):
    """Class named MFP."""
    def print(self, document):
        print(f"Printing document: {document}")

    def fax(self, document):
        pass

    def scan(self, document):
        raise NotImplementedError("Printer cannot scan!")

printer = OldFashionedPrinter()

printer.print("Hello world")
printer.fax("Test document")
printer.scan("Important document"),