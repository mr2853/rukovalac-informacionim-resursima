import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox
from pocetna_strana import PocetnaStrana

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    pocetna_strana = PocetnaStrana()
    with open("src/style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    
    app.exec_()
    if hasattr(pocetna_strana, "csor"):
        pocetna_strana.csor.close()
        pocetna_strana.connection.close()
        
    sys.exit()