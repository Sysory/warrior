# Form implementation generated from reading ui file 'A:\warrior\distribution.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(243, 244)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 20, 61, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.rBtn_2 = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.rBtn_2.setObjectName("rBtn_2")
        self.gridLayout.addWidget(self.rBtn_2, 1, 0, 1, 1)
        self.rBtn_3 = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.rBtn_3.setObjectName("rBtn_3")
        self.gridLayout.addWidget(self.rBtn_3, 2, 0, 1, 1)
        self.rBtn_1 = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.rBtn_1.setObjectName("rBtn_1")
        self.gridLayout.addWidget(self.rBtn_1, 0, 0, 1, 1)
        self.TcInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.TcInput.setGeometry(QtCore.QRect(90, 80, 113, 20))
        self.TcInput.setObjectName("TcInput")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 120, 193, 69))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.VehicleInput1 = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.VehicleInput1.setObjectName("VehicleInput1")
        self.verticalLayout.addWidget(self.VehicleInput1)
        self.VehicleInput2 = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.VehicleInput2.setObjectName("VehicleInput2")
        self.verticalLayout.addWidget(self.VehicleInput2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.BtnCalculate = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.BtnCalculate.setFont(font)
        self.BtnCalculate.setObjectName("BtnCalculate")
        self.horizontalLayout_2.addWidget(self.BtnCalculate)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 243, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Распределение"))
        self.rBtn_2.setText(_translate("MainWindow", "11 - 20"))
        self.rBtn_3.setText(_translate("MainWindow", "21 - Tc"))
        self.rBtn_1.setText(_translate("MainWindow", "1 - 10"))
        self.TcInput.setPlaceholderText(_translate("MainWindow", "Tc = "))
        self.label.setText(_translate("MainWindow", "Кол - во техники"))
        self.BtnCalculate.setText(_translate("MainWindow", "Рассчитать"))
