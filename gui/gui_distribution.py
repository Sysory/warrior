import sys

from matplotlib import pyplot as plt
from PyQt6.QtCore import QSize, Qt
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import distrib_design
import distribution
from InputData import InputData

class ExampleApp(QtWidgets.QMainWindow, distrib_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.algorithmId : int = 0
        
        self.TcInput.setDisabled(True)
        self.TcInput.setPlaceholderText("Tc")
        self.rBtn_1.pressed.connect(self.rBtn1Handler)
        self.rBtn_2.pressed.connect(self.rBtn2Handler)
        self.rBtn_3.pressed.connect(self.rBtn3Handler)
        self.BtnCalculate.pressed.connect(self.BtnCalculateHandler)

    def rBtn1Handler(self):
        self.VehicleInput1.setPlaceholderText("v1")
        self.VehicleInput2.setDisabled(False)
        self.TcInput.setDisabled(True)
        self.VehicleInput2.setPlaceholderText("v2")
        self.algorithmId = 0

    def rBtn2Handler(self):
        self.VehicleInput1.setPlaceholderText("v2")
        self.VehicleInput2.setPlaceholderText("")
        self.VehicleInput2.setDisabled(True)
        self.TcInput.setDisabled(True)
        self.algorithmId = 1

    def rBtn3Handler(self):
        self.VehicleInput1.setPlaceholderText("v2")
        self.VehicleInput2.setDisabled(False)
        self.VehicleInput2.setPlaceholderText("v3")
        self.TcInput.setDisabled(False)
        self.TcInput.setPlaceholderText("Tc")
        self.algorithmId = 2

    def BtnCalculateHandler(self):
        self.data = InputData()
        val1, val2, Tc = 0, 0, 0
        try: val1 = int(self.VehicleInput1.text())
        except: pass

        try: val2 = int(self.VehicleInput2.text())
        except: pass

        try: Tc = int(self.TcInput.text())
        except: pass

        selectedAlgorithm : function = None
        xData : list[int] = []

        if (self.algorithmId == 0):
            selectedAlgorithm = distribution._1to10
            self.data.v1 = val1
            self.data.v2 = val2
            xData = [*range(1, 11)]
        elif (self.algorithmId == 1):
            selectedAlgorithm = distribution._11to20
            self.data.v2 = val1
            xData = [*range(11, 21)]
        elif (self.algorithmId == 2):
            selectedAlgorithm = distribution._over20
            self.data.v2 = val1
            self.data.v3 = val2
            self.data.Tc = Tc
            xData = [*range(21, self.data.Tc + 1)]

        distributedVehicles : list[int] = selectedAlgorithm(self.data)
        QtWidgets.QMessageBox.information(self, "Result", "Result: " + str(distributedVehicles))
        plt.plot(xData, distributedVehicles)
        plt.grid(visible=True)
        plt.show()
        
            
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение

if __name__ == '__main__':
    main()