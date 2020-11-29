import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox
from login import LoginForm
from PocetnaStrana import PocetnaStrana

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # form = LoginForm()
    # form.show()
    # with open("style.qss", "r") as f:
    #     _style = f.read()
    #     app.setStyleSheet(_style)

    pocetnaStrana = PocetnaStrana()
    
    sys.exit(app.exec_())