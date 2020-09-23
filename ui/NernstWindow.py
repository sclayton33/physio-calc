# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nernstwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NernstWindow(object):
    def setupUi(self, NernstWindow):
        NernstWindow.setObjectName("NernstWindow")
        NernstWindow.resize(800, 400)
        self.centralwidget = QtWidgets.QWidget(NernstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.valence = QtWidgets.QLineEdit(self.centralwidget)
        self.valence.setMaximumSize(QtCore.QSize(200, 16777215))
        self.valence.setObjectName("valence")
        self.gridLayout_2.addWidget(self.valence, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 2, 1, 1)
        self.xout = QtWidgets.QLineEdit(self.centralwidget)
        self.xout.setMaximumSize(QtCore.QSize(200, 16777215))
        self.xout.setObjectName("xout")
        self.gridLayout_2.addWidget(self.xout, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 2, 1, 1)
        self.xin = QtWidgets.QLineEdit(self.centralwidget)
        self.xin.setMaximumSize(QtCore.QSize(200, 16777215))
        self.xin.setClearButtonEnabled(False)
        self.xin.setObjectName("xin")
        self.gridLayout_2.addWidget(self.xin, 3, 1, 1, 1)
        self.temp = QtWidgets.QLineEdit(self.centralwidget)
        self.temp.setMaximumSize(QtCore.QSize(200, 16777215))
        self.temp.setInputMask("")
        self.temp.setText("")
        self.temp.setObjectName("temp")
        self.gridLayout_2.addWidget(self.temp, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.calculate = QtWidgets.QPushButton(self.splitter)
        self.calculate.setMaximumSize(QtCore.QSize(100, 25))
        self.calculate.setWhatsThis("")
        self.calculate.setObjectName("calculate")
        self.clear = QtWidgets.QPushButton(self.splitter)
        self.clear.setMaximumSize(QtCore.QSize(100, 25))
        self.clear.setWhatsThis("")
        self.clear.setObjectName("clear")
        self.gridLayout.addWidget(self.splitter, 0, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.veq = QtWidgets.QLineEdit(self.centralwidget)
        self.veq.setMaximumSize(QtCore.QSize(150, 16777215))
        self.veq.setObjectName("veq")
        self.gridLayout.addWidget(self.veq, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_9.setToolTip("")
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)
        NernstWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NernstWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        NernstWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NernstWindow)
        self.statusbar.setObjectName("statusbar")
        NernstWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NernstWindow)
        QtCore.QMetaObject.connectSlotsByName(NernstWindow)

    def retranslateUi(self, NernstWindow):
        _translate = QtCore.QCoreApplication.translate
        NernstWindow.setWindowTitle(_translate("NernstWindow", "Equilibrium Potential (Nernst potential)"))
        self.label_2.setText(_translate("NernstWindow", "Temperature (Kelvin):"))
        self.valence.setPlaceholderText(_translate("NernstWindow", "+1, +2, ... etc."))
        self.label_3.setText(_translate("NernstWindow", "Valence:"))
        self.label_8.setText(_translate("NernstWindow", "mM"))
        self.xout.setPlaceholderText(_translate("NernstWindow", "[X] in ECF"))
        self.label_7.setText(_translate("NernstWindow", "mM"))
        self.xin.setPlaceholderText(_translate("NernstWindow", "[X] in ICF"))
        self.temp.setPlaceholderText(_translate("NernstWindow", "e.g. 310 K"))
        self.label_4.setText(_translate("NernstWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">X</span><span style=\" font-size:16pt; vertical-align:sub;\">out</span><span style=\" font-size:16pt;\">:</span></p></body></html>"))
        self.label_5.setText(_translate("NernstWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">X</span><span style=\" font-size:16pt; vertical-align:sub;\">in</span><span style=\" font-size:16pt;\">:</span></p></body></html>"))
        self.calculate.setText(_translate("NernstWindow", "Calculate"))
        self.clear.setText(_translate("NernstWindow", "Clear"))
        self.label_6.setText(_translate("NernstWindow", "<html><head/><body><p><span style=\" font-weight:600;\">V</span><span style=\" font-weight:600; vertical-align:sub;\">Eq.</span><span style=\" font-weight:600;\">, Equilibrium Potential = </span></p></body></html>"))
        self.label_9.setText(_translate("NernstWindow", "mV"))
