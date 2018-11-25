import sys
import os.path

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, \
    QSizePolicy, QListWidget, QListWidgetItem, QInputDialog, QLineEdit, QMessageBox


def center(window):
    """ centers window """
    qr = window.frameGeometry()
    qr.moveCenter(QDesktopWidget().availableGeometry().center())
    window.move(qr.topLeft())


def text_dialog(parent, title, question):
    """ gets text """
    text, ok_pressed = QInputDialog.getText(parent, title, question, QLineEdit.Normal)
    if ok_pressed and text:
        return text
    else:
        return None


"""
class WelcomeWindow(QWidget):
    """""" Optional welcome page """"""
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(os.path.join(os.pardir, "res","logo.png")))
        self.setWindowTitle("QUIZZO LEARN - WITAJ !!!")
        self.resize(900,650)
        center(self)

        next_button = QPushButton("START")
        next_button.clicked.connect(self.next)
        vbox = QVBoxLayout()
        vbox.addWidget(next_button)

        self.setLayout(vbox)
        self.show()

    def next(self):
        self.close()
        menu_window.init_ui()
"""


class MyQListWidgetItem(QListWidgetItem):
    """My own QListWidgetItem"""

    def __init__(self, id=0, frase1="", frase2="", is_empty=False):
        super().__init__()
        self.id = id
        self.frase1 = frase1
        self.frase2 = frase2
        self.is_empty = is_empty


class QItem(QWidget):
    """ a simple widget for MyQListWidgetItem"""

    def __init__(self, id, frase1, frase2, parent=None):
        super().__init__()
        self.id = id
        delete_button = QPushButton("")
        delete_button.setIcon(QIcon(os.path.join(os.pardir, "res", "delete-icon.png")))
        delete_button.setIconSize(QSize(40, 40))
        delete_button.setStyleSheet("background-color: black;")
        delete_button.clicked.connect(self.delete_button_act)

        label1 = QLabel(frase1)
        label2 = QLabel(frase2)

        layout = QHBoxLayout()
        layout.addWidget(label1, 5)
        layout.addWidget(QLabel("="), 1)
        layout.addWidget(label2, 5)
        layout.addWidget(delete_button)

        self.setLayout(layout)

    def delete_button_act(self):
        new_test_window.deleting(self.id)


class MenuWindow(QWidget):
    """main menu"""

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(os.path.join(os.pardir, "res", "logo.png")))
        self.setWindowTitle("QUIZZO LEARN")
        self.resize(900, 650)
        center(self)
        self.load_ui()
        self.init_ui()

    def init_ui(self):
        self.show()

    def load_ui(self):
        mytests_button = QPushButton("MOJE TESTY")
        newtest_button = QPushButton("DODAJ TEST")
        bigtest_button = QPushButton("ZBUDUJ SPRAWDZIAN")

        mytests_button.setSizePolicy(QSizePolicy.Expanding,
                                     QSizePolicy.Preferred)
        newtest_button.setSizePolicy(QSizePolicy.Expanding,
                                     QSizePolicy.Preferred)
        bigtest_button.setSizePolicy(QSizePolicy.Expanding,
                                     QSizePolicy.Preferred)

        mytests_button.setStyleSheet("background-color: DarkOrange")
        newtest_button.setStyleSheet("background-color: DarkOrange")
        bigtest_button.setStyleSheet("background-color: DarkOrange")

        font = QFont("Serif", 20)
        mytests_button.setFont(font)
        newtest_button.setFont(font)
        bigtest_button.setFont(font)

        newtest_button.clicked.connect(self.newtest_act)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(mytests_button, 2)
        vbox.addStretch(1)
        vbox.addWidget(newtest_button, 2)
        vbox.addStretch(1)
        vbox.addWidget(bigtest_button, 2)
        vbox.addStretch(1)

        hbox = QHBoxLayout()

        hbox.addStretch(1)
        hbox.addLayout(vbox, 3)
        hbox.addStretch(1)
        self.setLayout(hbox)

    def newtest_act(self):
        test_name = text_dialog(self, "NAZWIJ SWÓJ TEST", "PODAJ NAZWĘ TESTU")
        if test_name is not None:
            self.close()
            new_test_window.init_ui(test_name)


class NewTestWindow(QWidget):
    """ adding new test"""

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(os.path.join(os.pardir, "res", "logo.png")))
        self.setWindowTitle("QUIZZO LEARN")
        self.resize(900, 650)
        center(self)
        self.load_ui()

    def init_ui(self, test_name):
        self.test_name = test_name
        self.number_of_frases = 0
        self.show()

    def load_ui(self):
        back_button = QPushButton("<= WRÓĆ")
        back_button.setStyleSheet("background-color: YellowGreen")
        back_button.clicked.connect(self.back_button_act)

        add_button = QPushButton()
        add_button.setIcon(QIcon(os.path.join(os.pardir, "res", "add-icon.png")))
        add_button.setIconSize(QSize(100, 100))
        add_button.setSizePolicy(QSizePolicy.Expanding,
                                 QSizePolicy.Preferred)
        add_button.clicked.connect(self.add)

        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addWidget(add_button, 1)
        vbox.addStretch(2)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(back_button)
        hbox2.addStretch(4)

        self.QList = QListWidget()
        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox2)
        vbox2.addWidget(self.QList)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox2, 7)
        hbox.addLayout(vbox, 1)

        self.setLayout(hbox)

    def back_button_act(self):
        alert = QMessageBox().warning(self,"JESTEŚ PEWIEN ??", 'UWAGA !!! \n STRACISZ WPROWADZONE SŁOWA \n JESTEŚ PEWIEN ??', QMessageBox.Yes, QMessageBox.No)
        if alert == QMessageBox.Yes:
            self.close()
            menu_window.show()

    def add(self):
        frase1 = text_dialog(self, "FRAZA 1", "  PODAJ PROSZĘ FRAZĘ 1")
        frase2 = text_dialog(self, "FRAZA 2", "  PODAJ PROSZĘ FRAZĘ 2")

        if not (frase1 is None or frase2 is None):
            item = MyQListWidgetItem(self.number_of_frases, frase1, frase2)

            widget_item = QItem(self.number_of_frases, frase1, frase2)
            item.setSizeHint(widget_item.sizeHint())

            self.number_of_frases += 1

            self.QList.addItem(item)
            self.QList.setItemWidget(item, widget_item)

    def deleting(self, id):
        i = 0
        i2 = self.QList.count()
        while i < i2:
            item = self.QList.item(i)
            if item.id == id:
                self.QList.removeItemWidget(item)
                item.is_empty = False
            i += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # welcome_window = WelcomeWindow()
    menu_window = MenuWindow()
    new_test_window = NewTestWindow()
    sys.exit(app.exec_())
