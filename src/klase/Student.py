class Student:
    def __init__(self, index, name, lastname, parent):
        super().__init__(parent)
        self.index = index
        self.name = name
        self.lastname = lastname