import time
from selenium import webdriver
from PyQt5 import QtCore, QtWidgets, QtGui
from screen import Ui_Form
import sys

class desbloqueador(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(desbloqueador, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon(".\Images\Icon.ico"))
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.botaohenry.clicked.connect(self.desbloquearhenry)
        self.botaocontrolid.clicked.connect(self.desbloquearcontrolid)
        self.botaofechar.clicked.connect(self.sairapp)


    def sairapp(self):
        print("Saindo até mais =3")
        sys.exit()

    def desbloquearhenry(self):
        nav = webdriver.Chrome(".\Driver\chromedriver.exe")
        nav.get("http://desbloqueio.ddns.net:8060/HENRY-1697532145/TamperUnblockClient/sessionExpired.xhtml")
        nav.find_element_by_name('j_idt14:j_idt17').click()
        time.sleep(1.5)
        nav.find_element_by_name('j_idt15:j_idt25').send_keys("danilo.do.carmo.toledo")
        nav.find_element_by_name('j_idt15:j_idt27').send_keys("dc15817")
        nav.find_element_by_name('j_idt15:txCpf').click()
        nav.find_element_by_name('j_idt15:txCpf').send_keys("37939215817")
        nav.find_element_by_name('j_idt15:j_idt30').click()

    def desbloquearcontrolid(self):
        nav = webdriver.Chrome(".\Driver\chromedriver.exe")
        nav.get("http://painel.controlid.com.br/login.aspx")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = desbloqueador()
    Form.show()
    sys.exit(app.exec_())



