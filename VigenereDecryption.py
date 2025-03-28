# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VigenereDecryption.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import re
from PyQt5 import QtCore, QtGui, QtWidgets

class VigenereCipher(object):

    def __init__(self):

        self.TablulaRecta = self.RectaCreate()

    def RectaCreate(self):

        TabulaRecta = []

        for i in range(0, 26):

            Reset = 0
            Row = []

            for Column in range(0, 26):
                Row.append(chr(i + 65 + Reset))
                Reset += 1
                if Reset > (25 - i):
                    Reset = Reset - 26

            TabulaRecta.append(Row)

        return TabulaRecta

    def encipher(self, PlainText, Keyword):

        PlainText = self.PlainTextInitialization(PlainText)
        RepeatedKeyWord = self.RepKey(Keyword, len(PlainText))
        CipherText = []

        for NoOf, Letter in enumerate(PlainText):

            IndexPlainText = ord(Letter.upper()) - 65
            IndexKey = ord(RepeatedKeyWord[NoOf]) - 65

            EncipheredText = self.TablulaRecta[IndexKey][IndexPlainText]

            CipherText.append(EncipheredText)

        return "".join(CipherText)

    def decipher(self, CipherText, KeyWord):

        keywordrepeated = self.RepKey(KeyWord, len(CipherText))
        PlainText = []

        for NoOf, Letter in enumerate(CipherText):

            keywordindex = ord(keywordrepeated[NoOf]) - 65

            DecipheredCharacter = chr(self.TablulaRecta[keywordindex].index(Letter) + 65)

            PlainText.append(DecipheredCharacter)

        return "".join(PlainText)

    def PlainTextInitialization(self, PlainText):

        PlainText = PlainText.upper()
        PlainText = re.sub("[^A-Z]", "", PlainText)

        return PlainText

    def RepKey(self, Key, Length):

        Key = Key.upper()
        Repeated = []
        KeyLength = len(Key)
        IndexKey = 0

        for i in range(0, Length):
            Repeated.append(Key[IndexKey])
            IndexKey += 1
            if IndexKey > KeyLength - 1:
                IndexKey = 0

        return "".join(Repeated)


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 491)
        self.decryptbutton = QtWidgets.QPushButton(Dialog)
        self.decryptbutton.setGeometry(QtCore.QRect(300, 290, 111, 41))
        self.decryptbutton.setStyleSheet("QPushButton {\n"
                                         "  padding: 8px 25px;\n"
                                         "\n"
                                         "  text-align: center;\n"
                                         "  outline: none;\n"
                                         "  color: #fff;\n"
                                         "  background-color:     #008000;\n"
                                         "  border: none;\n"
                                         "  border-radius: 15px;\n"
                                         "font: 15pt \"Rockwell\";\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {background-color: #006400}")
        self.decryptbutton.setObjectName("decryptbutton")
        self.decryptbutton.clicked.connect(self.Decrypt)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 711, 491))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/Vigenere.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(230, 40, 301, 51))
        self.label_3.setStyleSheet("color: rgb(253, 250, 255);\n"
                                   "font: 30pt \"Rockwell\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(240, 50, 291, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.Plaintext = QtWidgets.QTextBrowser(Dialog)
        self.Plaintext.setGeometry(QtCore.QRect(100, 380, 521, 41))
        self.Plaintext.setStyleSheet("  padding: 5px 20px;\n"
                                     "\n"
                                     "  text-align: center;\n"
                                     "  outline: none;\n"
                                     "  background-color:     #f7f7f7;\n"
                                     "  border: none;\n"
                                     "  border-radius: 15px;\n"
                                     "font: 14pt \"Futura\";")
        self.Plaintext.setObjectName("Plaintext")
        self.Ciphertext_2 = QtWidgets.QLineEdit(Dialog)
        self.Ciphertext_2.setGeometry(QtCore.QRect(110, 140, 491, 41))
        self.Ciphertext_2.setStyleSheet("QLineEdit{\n"
                                        "  padding: 8px 20px;\n"
                                        "\n"
                                        "  text-align: center;\n"
                                        "  outline: none;\n"
                                        "  background-color:     #f7f7f7;\n"
                                        "  border: 2px solid rgb(194, 191, 196);\n"
                                        "  border-radius: 15px;\n"
                                        "font: 14pt \"Futura\";\n"
                                        "}\n"
                                        "QLineEdit:hover{\n"
                                        "border: 2px solid rgb(70, 69, 71);\n"
                                        "}\n"
                                        "QlineEdit:active{\n"
                                        "border: 2px solid rgb(0, 116, 0);\n"
                                        "}")
        self.Ciphertext_2.setObjectName("Ciphertext_2")
        self.key = QtWidgets.QLineEdit(Dialog)
        self.key.setGeometry(QtCore.QRect(110, 200, 251, 41))
        self.key.setStyleSheet("QLineEdit{\n"
                               "  padding: 8px 20px;\n"
                               "\n"
                               "  text-align: center;\n"
                               "  outline: none;\n"
                               "  background-color:     #f7f7f7;\n"
                               "  border: 2px solid rgb(194, 191, 196);\n"
                               "  border-radius: 15px;\n"
                               "font: 14pt \"Futura\";\n"
                               "}\n"
                               "QLineEdit:hover{\n"
                               "border: 2px solid rgb(70, 69, 71);\n"
                               "}\n"
                               "QlineEdit:active{\n"
                               "border: 2px solid rgb(0, 116, 0);\n"
                               "}")
        self.key.setObjectName("key")
        self.label.raise_()
        self.decryptbutton.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.Plaintext.raise_()
        self.Ciphertext_2.raise_()
        self.key.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.decryptbutton.setText(_translate("Dialog", "Decrypt"))
        self.label_3.setText(_translate("Dialog", "Vigenere Cipher"))
        self.label_5.setText(_translate("Dialog", "________________________________________"))
        self.Plaintext.setPlaceholderText(_translate("Dialog", "The Plaintext (Result)"))
        self.Ciphertext_2.setPlaceholderText(_translate("Dialog", "Enter the Ciphertext:"))
        self.key.setPlaceholderText(_translate("Dialog", "Enter the Key e.g. 'Love'"))

    def Decrypt(self):

        Ct = self.Ciphertext_2.text().upper()
        ky = self.key.text()

        final = VigenereCipher().decipher(Ct, ky)

        self.Plaintext.setText(final)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
