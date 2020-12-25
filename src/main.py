import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox
from pocetna_strana import PocetnaStrana

if __name__ == '__main__':
    app = QApplication(sys.argv) #inicijalizuje qt aplikaciju. Svaka Qt aplikacija mora imati application objekat, The sys.argv parameter is a list of argument from a command line. Ovim kontrolisemo start skripta
    
    pocetna_strana = PocetnaStrana()
    
    sys.exit(app.exec_()) #glavna petlja aplikacije, odavde sve krece 