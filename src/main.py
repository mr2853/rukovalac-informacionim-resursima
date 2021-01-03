import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox
from pocetna_strana import PocetnaStrana

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    pocetna_strana = PocetnaStrana()
    with open("src/style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    
    sys.exit(app.exec_())