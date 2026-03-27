from testing import *
from scanning import *
from printing import *

if __name__ == "__main__":

    printer = MyPrinter()
    photocopier = Photocopier()

    printer.print("Hello from printer")

    photocopier.print("Copy this document")
    photocopier.scan("Scanned document")

    mfm = MultiFunctionMachine(printer, photocopier)
    mfm.print("Delegated print")
    mfm.scan("Delegated scan")