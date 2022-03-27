from PyQt5 import QtCore, QtGui, QtWidgets
import sys, recursosui
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(470, 457)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setWindowIcon(QtGui.QIcon(".\Images\Icon.ico"))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 20, 450, 400))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 190, 350))
        self.label.setStyleSheet("border-image: url(:/Imagens/cadeado.png);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 241, 350))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(230, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_3.setObjectName("label_3")
        self.botaohenry = QtWidgets.QPushButton(self.widget)
        self.botaohenry.setGeometry(QtCore.QRect(225, 150, 191, 41))
        self.botaohenry.setStyleSheet("QPushButton{\n"
"border-radius:20px ;\n"
"background-color: rgb(250, 62, 100);\n"
"font: 20pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius:20px ;\n"
"    background-color: rgb(250, 126, 129);\n"
"font: 20pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.botaohenry.setObjectName("botaohenry")
        self.botaocontrolid = QtWidgets.QPushButton(self.widget)
        self.botaocontrolid.setGeometry(QtCore.QRect(225, 210, 191, 41))
        self.botaocontrolid.setStyleSheet("QPushButton{\n"
"border-radius:20px ;\n"
"background-color: rgb(250, 62, 100);\n"
"font: 20pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius:20px ;\n"
"    background-color: rgb(250, 126, 129);\n"
"font: 20pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.botaocontrolid.setObjectName("botaocontrolid")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(30, 320, 141, 31))
        self.label_4.setStyleSheet("border-image: url(:/Imagens/Logo.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.botaofechar = QtWidgets.QPushButton(self.widget)
        self.botaofechar.setGeometry(QtCore.QRect(415, 15, 21, 21))
        self.botaofechar.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botaofechar.setFont(font)
        self.botaofechar.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color: rgb(250, 62, 100);\n"
"font: 15pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius:10px ;\n"
"background-color: rgb(250, 126, 129);\n"
"font: 15pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.botaofechar.setObjectName("botaofechar")
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Desbloquear"))
        self.botaohenry.setText(_translate("Form", "HENRY"))
        self.botaocontrolid.setText(_translate("Form", "Control ID"))
        self.botaofechar.setText(_translate("Form", "x"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
