from printing import *
from scanning import *

class MyPrinter(Printer):
    def print_document(self, document):
        print(f"Printing document: {document}")

class Photocopier(Printer, Scanner):
    def scan_document(self, document):
        print(f"Scanning document: {document}")

    def print_document(self, document):
        print(f"Printing document: {document}")

class MultiFunctionMachine:
    def __init__(self, printer: Printer, scanner: Scanner):
        self.__printer = printer
        self._scanner = scanner

    def print_document(self, document):
        self.__printer.print_document(document)

    def scan_document(self, document):
        self._scanner.scan_document(document)

if __name__ == "__main__":

    printer = MyPrinter()
    photocopier = Photocopier()

    printer.print_document("Hello from printer")

    photocopier.print_document("Copy this document")
    photocopier.scan_document("Scanned document")

    mfm = MultiFunctionMachine(printer, photocopier)
    mfm.print_document("Delegated print")
    mfm.scan_document("Delegated scan")