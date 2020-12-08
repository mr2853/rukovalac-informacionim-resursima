import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox
from PySide2.QtGui import QIcon

class Prijava(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prijava")
        self.resize(500,300)

        layout = QGridLayout()
        icon = QIcon("logo.png")
        self.setWindowIcon(icon)
        korisnicko_ime = QLabel('<font size="4"> Korisnicko ime: </font>')
        self.line_edit_korisnik = QLineEdit()
        self.line_edit_korisnik.setPlaceholderText("Molim Vas unesite korisnicko ime: ")
        layout.addWidget(korisnicko_ime,0,0)
        layout.addWidget(self.line_edit_korisnik,0,1)

        lozinka = QLabel('<font size="4"> Lozinka: </font>')
        self.line_edit_lozinka = QLineEdit()
        self.line_edit_lozinka.setPlaceholderText("Molim Vas unesite lozinku:")
        layout.addWidget(lozinka,1,0)
        layout.addWidget(self.line_edit_lozinka,1,1)
        layout.setRowMinimumHeight(2,75)
        

        dugme = QPushButton("Prijavi se")
        dugme.clicked.connect(self.check_password)
        dugme2 = QPushButton("Dodaj novog korisnika")
        dugme.clicked.connect(self.check_password)
        layout.addWidget(dugme, 2,0,1,2)
        layout.addWidget(dugme2, 3,0,2,3)
        self.setLayout(layout)
    
    def check_password(self):
        msg = QMessageBox()

        if self.line_edit_korisnik.text() == "Vesna" and self.line_edit_lozinka.text() == "111":
            msg.setText("Ulogovani ste!")
            msg.exec_()
        else:
            msg.setText("Pogresna lozinka!")
            msg.exec_()

 

