# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tempcowindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TempcoWindow(object):
    def setupUi(self, TempcoWindow):
        TempcoWindow.setObjectName("TempcoWindow")
        TempcoWindow.resize(800, 400)
        self.centralwidget = QtWidgets.QWidget(TempcoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setMaximumSize(QtCore.QSize(16777215, 89))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setPixmap(QtGui.QPixmap("./resources/logo.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.t_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t_1.setMinimumSize(QtCore.QSize(200, 0))
        self.t_1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.t_1.setInputMask("")
        self.t_1.setText("")
        self.t_1.setObjectName("t_1")
        self.gridLayout_2.addWidget(self.t_1, 0, 1, 1, 1)
        self.celsius1 = QtWidgets.QRadioButton(self.centralwidget)
        self.celsius1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.celsius1.setChecked(True)
        self.celsius1.setObjectName("celsius1")
        self.gridLayout_2.addWidget(self.celsius1, 0, 2, 2, 1)
        self.kelvin1 = QtWidgets.QRadioButton(self.centralwidget)
        self.kelvin1.setChecked(False)
        self.kelvin1.setAutoExclusive(True)
        self.kelvin1.setObjectName("kelvin1")
        self.gridLayout_2.addWidget(self.kelvin1, 0, 3, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.t_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t_2.setMinimumSize(QtCore.QSize(200, 0))
        self.t_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.t_2.setObjectName("t_2")
        self.gridLayout_2.addWidget(self.t_2, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.r_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.r_1.setMinimumSize(QtCore.QSize(200, 0))
        self.r_1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.r_1.setInputMask("")
        self.r_1.setText("")
        self.r_1.setObjectName("r_1")
        self.gridLayout_3.addWidget(self.r_1, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.r_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.r_2.setMinimumSize(QtCore.QSize(200, 0))
        self.r_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.r_2.setObjectName("r_2")
        self.gridLayout_3.addWidget(self.r_2, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.calculate = QtWidgets.QPushButton(self.splitter)
        self.calculate.setMaximumSize(QtCore.QSize(100, 25))
        self.calculate.setObjectName("calculate")
        self.clear = QtWidgets.QPushButton(self.splitter)
        self.clear.setMaximumSize(QtCore.QSize(100, 25))
        self.clear.setObjectName("clear")
        self.gridLayout.addWidget(self.splitter, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_6.setIndent(-1)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.q_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.q_10.setMaximumSize(QtCore.QSize(200, 16777215))
        self.q_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.q_10.setObjectName("q_10")
        self.gridLayout.addWidget(self.q_10, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 2, 0, 1, 2)
        TempcoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TempcoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        TempcoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TempcoWindow)
        self.statusbar.setObjectName("statusbar")
        TempcoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TempcoWindow)
        QtCore.QMetaObject.connectSlotsByName(TempcoWindow)

    def retranslateUi(self, TempcoWindow):
        _translate = QtCore.QCoreApplication.translate
        TempcoWindow.setWindowTitle(_translate("TempcoWindow", "Temperature Coefficient"))
        self.label_2.setText(_translate("TempcoWindow", "<html><head/><body><p>T<span style=\" vertical-align:sub;\">1</span>:</p></body></html>"))
        self.t_1.setPlaceholderText(_translate("TempcoWindow", "temp when R1 measured"))
        self.celsius1.setText(_translate("TempcoWindow", "C"))
        self.kelvin1.setText(_translate("TempcoWindow", "K"))
        self.label_3.setText(_translate("TempcoWindow", "<html><head/><body><p>T<span style=\" vertical-align:sub;\">2</span>:</p></body></html>"))
        self.t_2.setPlaceholderText(_translate("TempcoWindow", "temp when R2 measured"))
        self.label_4.setText(_translate("TempcoWindow", "<html><head/><body><p>R<span style=\" vertical-align:sub;\">1</span>:</p></body></html>"))
        self.r_1.setPlaceholderText(_translate("TempcoWindow", "reaction rate at T1"))
        self.label_8.setText(_translate("TempcoWindow", "<html><head/><body><p>R<span style=\" vertical-align:sub;\">2</span>:</p></body></html>"))
        self.r_2.setPlaceholderText(_translate("TempcoWindow", "reaction rate at T2"))
        self.calculate.setWhatsThis(_translate("TempcoWindow", "<html><head/><body><p>Click to calculate the equilibrum potential.</p></body></html>"))
        self.calculate.setText(_translate("TempcoWindow", "Calculate"))
        self.clear.setWhatsThis(_translate("TempcoWindow", "<html><head/><body><p>Click to calculate the equilibrum potential.</p></body></html>"))
        self.clear.setText(_translate("TempcoWindow", "Clear"))
        self.label_6.setText(_translate("TempcoWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Q</span><span style=\" font-weight:600; vertical-align:sub;\">10</span><span style=\" font-weight:600;\">, Temperature Coefficient =</span></p></body></html>"))

