# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kantor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(428, 240)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.kwota1 = QtWidgets.QTextEdit(self.centralwidget)
        self.kwota1.setGeometry(QtCore.QRect(60, 60, 61, 31))
        self.kwota1.setObjectName("kwota1")
        self.wybor1 = QtWidgets.QComboBox(self.centralwidget)
        self.wybor1.setGeometry(QtCore.QRect(120, 60, 73, 31))
        self.wybor1.setObjectName("wybor1")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.wybor1.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 50, 21, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tloKwoty = QtWidgets.QTextEdit(self.centralwidget)
        self.tloKwoty.setGeometry(QtCore.QRect(230, 60, 61, 31))
        self.tloKwoty.setObjectName("tloKwoty")
        self.wybor2 = QtWidgets.QComboBox(self.centralwidget)
        self.wybor2.setGeometry(QtCore.QRect(290, 60, 73, 31))
        self.wybor2.setObjectName("wybor2")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.wybor2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 120, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.kwota3 = QtWidgets.QLabel(self.centralwidget)
        self.kwota3.setGeometry(QtCore.QRect(235, 60, 61, 30))
        self.kwota3.setMaximumSize(QtCore.QSize(200, 30))
        self.kwota3.setText("")
        self.kwota3.setObjectName("kwota3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.pushButton.clicked.connect(self.pressed)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.wybor1.setItemText(0, _translate("MainWindow", "PLN"))
        self.wybor1.setItemText(1, _translate("MainWindow", "THB"))
        self.wybor1.setItemText(2, _translate("MainWindow", "USD"))
        self.wybor1.setItemText(3, _translate("MainWindow", "AUD"))
        self.wybor1.setItemText(4, _translate("MainWindow", "HKD"))
        self.wybor1.setItemText(5, _translate("MainWindow", "CAD"))
        self.wybor1.setItemText(6, _translate("MainWindow", "NZD"))
        self.wybor1.setItemText(7, _translate("MainWindow", "SGD"))
        self.wybor1.setItemText(8, _translate("MainWindow", "EUR"))
        self.wybor1.setItemText(9, _translate("MainWindow", "HUF"))
        self.wybor1.setItemText(10, _translate("MainWindow", "CHF"))
        self.wybor1.setItemText(11, _translate("MainWindow", "GBP"))
        self.wybor1.setItemText(12, _translate("MainWindow", "UAH"))
        self.wybor1.setItemText(13, _translate("MainWindow", "JPY"))
        self.wybor1.setItemText(14, _translate("MainWindow", "CZK"))
        self.wybor1.setItemText(15, _translate("MainWindow", "DKK"))
        self.wybor1.setItemText(16, _translate("MainWindow", "ISK"))
        self.wybor1.setItemText(17, _translate("MainWindow", "NOK"))
        self.wybor1.setItemText(18, _translate("MainWindow", "SEK"))
        self.wybor1.setItemText(19, _translate("MainWindow", "HRK"))
        self.wybor1.setItemText(20, _translate("MainWindow", "RON"))
        self.wybor1.setItemText(21, _translate("MainWindow", "BGN"))
        self.wybor1.setItemText(22, _translate("MainWindow", "TRY"))
        self.wybor1.setItemText(23, _translate("MainWindow", "ILS"))
        self.wybor1.setItemText(24, _translate("MainWindow", "CLP"))
        self.wybor1.setItemText(25, _translate("MainWindow", "PHP"))
        self.wybor1.setItemText(26, _translate("MainWindow", "MXN"))
        self.wybor1.setItemText(27, _translate("MainWindow", "ZAR"))
        self.wybor1.setItemText(28, _translate("MainWindow", "BRL"))
        self.wybor1.setItemText(29, _translate("MainWindow", "MYR"))
        self.wybor1.setItemText(30, _translate("MainWindow", "RUB"))
        self.wybor1.setItemText(31, _translate("MainWindow", "IDR"))
        self.wybor1.setItemText(32, _translate("MainWindow", "INR"))
        self.wybor1.setItemText(33, _translate("MainWindow", "KRW"))
        self.wybor1.setItemText(34, _translate("MainWindow", "CNY"))
        self.wybor1.setItemText(35, _translate("MainWindow", "XDR"))
        self.label.setText(_translate("MainWindow", "="))
        self.wybor2.setItemText(0, _translate("MainWindow", "PLN"))
        self.wybor2.setItemText(1, _translate("MainWindow", "THB"))
        self.wybor2.setItemText(2, _translate("MainWindow", "USD"))
        self.wybor2.setItemText(3, _translate("MainWindow", "AUD"))
        self.wybor2.setItemText(4, _translate("MainWindow", "HKD"))
        self.wybor2.setItemText(5, _translate("MainWindow", "CAD"))
        self.wybor2.setItemText(6, _translate("MainWindow", "NZD"))
        self.wybor2.setItemText(7, _translate("MainWindow", "SGD"))
        self.wybor2.setItemText(8, _translate("MainWindow", "EUR"))
        self.wybor2.setItemText(9, _translate("MainWindow", "HUF"))
        self.wybor2.setItemText(10, _translate("MainWindow", "CHF"))
        self.wybor2.setItemText(11, _translate("MainWindow", "GBP"))
        self.wybor2.setItemText(12, _translate("MainWindow", "UAH"))
        self.wybor2.setItemText(13, _translate("MainWindow", "JPY"))
        self.wybor2.setItemText(14, _translate("MainWindow", "CZK"))
        self.wybor2.setItemText(15, _translate("MainWindow", "DKK"))
        self.wybor2.setItemText(16, _translate("MainWindow", "ISK"))
        self.wybor2.setItemText(17, _translate("MainWindow", "NOK"))
        self.wybor2.setItemText(18, _translate("MainWindow", "SEK"))
        self.wybor2.setItemText(19, _translate("MainWindow", "HRK"))
        self.wybor2.setItemText(20, _translate("MainWindow", "RON"))
        self.wybor2.setItemText(21, _translate("MainWindow", "BGN"))
        self.wybor2.setItemText(22, _translate("MainWindow", "TRY"))
        self.wybor2.setItemText(23, _translate("MainWindow", "ILS"))
        self.wybor2.setItemText(24, _translate("MainWindow", "CLP"))
        self.wybor2.setItemText(25, _translate("MainWindow", "PHP"))
        self.wybor2.setItemText(26, _translate("MainWindow", "MXN"))
        self.wybor2.setItemText(27, _translate("MainWindow", "ZAR"))
        self.wybor2.setItemText(28, _translate("MainWindow", "BRL"))
        self.wybor2.setItemText(29, _translate("MainWindow", "MYR"))
        self.wybor2.setItemText(30, _translate("MainWindow", "RUB"))
        self.wybor2.setItemText(31, _translate("MainWindow", "IDR"))
        self.wybor2.setItemText(32, _translate("MainWindow", "INR"))
        self.wybor2.setItemText(33, _translate("MainWindow", "KRW"))
        self.wybor2.setItemText(34, _translate("MainWindow", "CNY"))
        self.wybor2.setItemText(35, _translate("MainWindow", "XDR"))
        self.pushButton.setText(_translate("MainWindow", "PRZELICZ"))
        self.load = True
        

    def pressed(self):
    
        ################
        if self.load == True:
            self.load = False
            from bs4 import BeautifulSoup
            from requests import get

            url = 'https://www.nbp.pl/home.aspx?f=/kursy/kursya.html'

            page = get(url)

            bs = BeautifulSoup(page.content, 'html.parser')

            a = bs.find('tbody')
            self.waluta = []
            self.wartosc = []
            licz = 0
            for i in a:
                if len(i)>=2:
                    b = i.find_all('td', class_="right")
                    for i in b:
                        licz += 1
                        if licz%2 == 0:
                            if count > 0:
                                bufor1 = float((i.get_text().replace(',','.')))/(10**count)
                                self.wartosc.append(bufor1)
                            else:
                                self.wartosc.append(float((i.get_text().replace(',','.'))))

                        else:
                            bufor2 = (i.get_text().replace('1','').replace(' ',''))
                            count = bufor2.count('0')
                            self.waluta.append((i.get_text().replace('1','').replace('0','').replace(' ','')))
                    licz = 0

        ################################################################
                    
        x = self.wybor1.currentText()
        y = self.wybor2.currentText()
 
        if x == 'PLN' and y != 'PLN':
            k1 = float(self.kwota1.toPlainText())
            index = self.waluta.index(y)
            k2 = float(self.wartosc[index])
            print('k1',k1)
            print('k2',k2)
            wynik = k1/k2
            self.kwota3.setText(str(round(wynik,2)))
        elif x != 'PLN' and y == 'PLN':
            k1 = float(self.kwota1.toPlainText())
            index = self.waluta.index(x)
            k2 = float(self.wartosc[index])
            wynik = k1*k2
            self.kwota3.setText(str(round(wynik,2)))
        else:
            index1 = self.waluta.index(y)
            k1 = float(self.kwota1.toPlainText())
            index2 = self.waluta.index(y)
            k2 = float(self.wartosc[index2])
            print('k1',k1)
            print('k2',k2)
            wynik = k1/k2
            self.kwota3.setText(str(round(wynik,2)))
       
                    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())
    
 
