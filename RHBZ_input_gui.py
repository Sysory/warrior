import sys

from matplotlib import pyplot as plt
from PyQt6.QtCore import QSize, Qt
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import RHBZ_design
import knapsak_solve_original
import distribution
from RHBZ_input import RHBZ_input

class ExampleApp(QtWidgets.QMainWindow, RHBZ_design.Ui_RHBZ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Calculate.pressed.connect(self.btnCalculateHandler)
        self.rBtn1.pressed.connect(self.rBtn1Handler)
        self.rBtn2.pressed.connect(self.rBtn2Handler)
        self.rBtn3.pressed.connect(self.rBtn3Handler)

        self.fields : list[QtWidgets.QLineEdit] = [
            self.Park_capacity,
            self.Price_buy_0,
            self.Price_buy_1,
            self.Price_rep_0,
            self.Price_rep_1,
            self.Money_year,
            self.Money_year_vol,
            self.Obsolete_age,
            self.Population_size,
            self.Max_generation,
            self.P_mutate,
            self.P_crossover,
            self.VInput1,
            # self.VInput2,
            # self.InputTc,
        ]

        self.algorithmId = 0

    # западло разбираться как получить детей из формы
    def isAnyFieldEmpty(self):
        for field in self.fields:
            if (field.text() == ""): return True
        return False

    def rBtn1Handler(self):
        self.VInput1.setPlaceholderText("v1")
        self.VInput2.setDisabled(False)
        self.TcInput.setDisabled(True)
        self.VInput2.setPlaceholderText("v2")
        self.algorithmId = 0

    def rBtn2Handler(self):
        self.VInput1.setPlaceholderText("v2")
        self.VInput2.setPlaceholderText("")
        self.VInput2.setDisabled(True)
        self.TcInput.setDisabled(True)
        self.algorithmId = 1

    def rBtn3Handler(self):
        self.VInput1.setPlaceholderText("v2")
        self.VInput2.setDisabled(False)
        self.VInput2.setPlaceholderText("v3")
        self.TcInput.setDisabled(False)
        self.TcInput.setPlaceholderText("Tc")
        self.algorithmId = 2

    def btnCalculateHandler(self):
        if (self.isAnyFieldEmpty()):
            msgBox = QtWidgets.QMessageBox(text = "Заполните все поля")
            msgBox.exec()
            return None
        
        #запуск ф-ии из knapsak solve original, передав ей self и RHBZ input
        inputData = RHBZ_input()

        inputData.parkCapacity = int(self.Park_capacity.text())
        inputData.priceBuy = [
            float(self.Price_buy_0.text()),
            float(self.Price_buy_1.text())
        ]
        inputData.priceRep = [
            float(self.Price_rep_0.text()),
            float(self.Price_rep_1.text())
        ]
        inputData.moneyYear = float(self.Money_year.text())
        inputData.moneyYearVol = float(self.Money_year_vol.text())
        inputData.obsoleteAge = int(self.Obsolete_age.text())

        inputData.populationSize = int(self.Population_size.text())
        inputData.maxGenerations = int(self.Max_generation.text())
        inputData.pMutate = float(self.P_mutate.text())
        inputData.pCrossover = float(self.P_crossover.text())

        selectedAlgorithm : function = None

        if (self.algorithmId == 0):
            selectedAlgorithm = distribution._1to10
            inputData.v1 = int(self.VInput1.text())
            inputData.v2 = int(self.VInput2.text())
        elif (self.algorithmId == 1):
            selectedAlgorithm = distribution._11to20
            inputData.v2 = int(self.VInput1.text())
        elif (self.algorithmId == 2):
            selectedAlgorithm = distribution._over20
            inputData.v2 = int(self.VInput1.text())
            inputData.v3 = int(self.VInput2.text())
            inputData.Tc = int(self.TcInput.text())

        inputData.algorithmId = self.algorithmId
        inputData.listAges = selectedAlgorithm(inputData)
        knapsak_solve_original.main(inputData)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение

if __name__ == '__main__':
    main()