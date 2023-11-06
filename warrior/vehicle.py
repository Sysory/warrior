from RHBZ_input import RHBZ_input
from random import randint as rd

class VehiclePark():
    types = ["rhm_6", "rhm_8"]
    # repairCost = 1.7
    # maxAmount = 200
    penaltyBuy = 10
    penaltyRepair = 10

    def __init__(self, inputData : RHBZ_input):
        self.inputData = inputData
        self.park : list[Vehicle] = list()  #TODO сделать класс VehiclePark итерируемым, чтобы убрать self.park
        self.money = inputData.moneyYear
        self.moneyYear = inputData.moneyYear
        self.moneyVol = inputData.moneyYearVol
    
    def passYear(self):
        self.money = self.moneyYear + (self.moneyYear * self.moneyVol / 100.) 
        self.writeOff()
        for vehicle in self.park:
            vehicle.age += 1
            if (vehicle.onRepair):
                if (vehicle.timeToRepair > 0):
                    vehicle.timeToRepair -= 1
                else:
                    vehicle.Repair()

    ## Добавление техники в парк без покупки (для внутренних целей)
    def addVehicle(self, type, age = 0):
        vehicle : Vehicle = None
        ###TODO заменить types на перечисление
        if type == VehiclePark.types[0]:    # rhm_6
            vehicle = Rhm_6(inputData=self.inputData, age=age)
        elif type == VehiclePark.types[1]:  # rhm_8
            vehicle = Rhm_8(inputData=self.inputData, age = age)

        if (len(self) < self.inputData.parkCapacity):
            self.park.append(vehicle)
        return vehicle
    
    def getBroken(self, type = "") -> int:
        broken = 0
        for vehicle in self.park:
            if vehicle.type == type or type == "":
                # broken += vehicle.isBroken  and not vehicle.onRepair
                broken += vehicle.isBroken
        return broken

    def getModern(self, type = "") -> int:
        modern = 0
        for vehicle in self.park:
            if vehicle.type == type or type == "":
                modern += vehicle.isModern
        return modern

    def getTotalCost(self):
        totalCost = 0
        for vehicle in self.park:
            totalCost += vehicle.cost
        return totalCost
    
    def getTotalCost(self, type : str):
        totalCost = 0
        for vehicle in self.park:
            if vehicle.type == type:
                totalCost += vehicle.cost
        return totalCost

    def getTotalEfficiency(self, type : str = ""):
        totalEfficiency = 0
        for vehicle in self.park:
            if vehicle.type == type or type == "":
                totalEfficiency += vehicle.getEfficiency()
        return totalEfficiency

    def buyNew(self, type, amount = 1):
        penalty = 0.0
        vehicle : Vehicle = None
        for i in range(amount):
            if (len(self) >= self.inputData.parkCapacity):
                return max(penalty, VehiclePark.penaltyBuy * (amount - i))
                # return max(penalty, VehiclePark.penaltyBuy * 10)
            if type == VehiclePark.types[0]:
                vehicle = Rhm_6(inputData=self.inputData, age = 0)
            elif type == VehiclePark.types[1]:
                vehicle = Rhm_8(inputData=self.inputData, age = 0)

            if (vehicle.cost <= self.money):
                self.money -= vehicle.cost
                self.park.append(vehicle)
            else:
                penalty += VehiclePark.penaltyBuy * 10
        return penalty


    def writeOff(self):
        if (self.inputData.Tc == 0): self.inputData.Tc = 25
        for vehicle in self.park:
            # if vehicle.age >= self.obsoleteAge:
            if vehicle.age >= self.inputData.Tc:
                self.park.remove(vehicle)

    def sendToRepair(self, type, amount):
        penalty = 0.0
        broken = self.getBroken(type)

        if (amount > broken):
            penalty += (amount - broken) * (VehiclePark.penaltyRepair+1)
            amount = broken

        needToRepair = amount
        for vehicle in self.park:
            if needToRepair == 0: break
            if vehicle.type == type:
                if vehicle.repairCost <= self.money:
                    #vehicle.Repair()
                    vehicle.onRepair = True
                    needToRepair -= 1
                    self.money -= vehicle.repairCost
                else:
                    penalty += VehiclePark.penaltyRepair
        return penalty

    def __len__(self):
        return len(self.park)


class Vehicle():
    def __init__(self, inputData : RHBZ_input, age : int = 0):
        self.inputData = inputData
        self.type = ""
        self.age = age
        self.isBroken : bool = False
        self.isModern : bool = True
        self.onRepair : bool = False
        self.cost : float = 0
        self.repairCost : float = 0
        self.eff : float = 0
        #self.timeToRepair = rd(1, 3) #TODO добавить возможность случайного времени ремонта
        self.timeToRepair = 0

    def Break(self):
        self.isBroken = True

    def Repair(self):
        self.isBroken = False
        self.onRepair = False

    def Obsolete(self):
        self.isModern = False

    def getEfficiency(self):
        if self.isBroken:
            return 0
        elif not self.isModern:
            return self.eff / 2
        else:
            return self.eff

class Rhm_6(Vehicle):
    def __init__(self, inputData : RHBZ_input, age : int = 0):
        super().__init__(inputData, age)
        # print(f"{self.age}, {self.isBroken}")
        # self.age = age
        self.type = VehiclePark.types[0]
        # self.cost = 10
        self.cost = self.inputData.priceBuy[0]  # TODO заменить на словарь
        self.repairCost = self.inputData.priceRep[0]
        self.eff = 3.0 / 250 * 14   # не используется, абстрактное значение из головы

class Rhm_8(Vehicle):
    def __init__(self, inputData : RHBZ_input, age : int = 0):
        super().__init__(inputData, age)
        # self.age = age
        self.type = VehiclePark.types[1]
        # self.cost = 15
        self.cost = self.inputData.priceBuy[1]
        self.repairCost = self.inputData.priceRep[1]
        self.eff = 3.0 / 250 * 21
