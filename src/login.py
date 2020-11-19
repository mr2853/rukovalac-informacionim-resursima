import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Form")
        self.resize(500,300)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText("Please enter your username: ")
        layout.addWidget(label_name,0,0)
        layout.addWidget(self.lineEdit_username,0,1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("Please enter your username")
        layout.addWidget(label_password,1,0)
        layout.addWidget(self.lineEdit_password,1,1)
        layout.setRowMinimumHeight(2,75)
        

        button = QPushButton("Login")
        button.clicked.connect(self.check_password)
        button2 = QPushButton("Add new user")
        button.clicked.connect(self.check_password)
        layout.addWidget(button, 2,0,1,2)
        layout.addWidget(button2, 3,0,2,3)
        self.setLayout(layout)
    
    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == "Vesna" and self.lineEdit_password.text() == "111":
            msg.setText("You are in")
            msg.exec_()
        else:
            msg.setText("Incorrect Password")
            msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = LoginForm()
    form.show()
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec_())