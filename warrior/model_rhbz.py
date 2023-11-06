import random
import numpy as np
from random import randint as rd

from RHBZ_input import RHBZ_input
from vehicle import *

class Knapsack01Problem:
    def __init__(self, inputData : RHBZ_input):
        self.inputData = inputData
        random.seed(1)
        # initialize instance variables:
        self.park = VehiclePark(inputData)
        # self.AGES : list[int] = [x for x in range(0, 11)]
        # self.normAGES : list[float] = list(np.array(self.AGES) / max(self.AGES))
        # initialize the data:
        self.__initData()

    def __len__(self):
        """
        :return: the total number of items defined in the problem
        """
        return len(self.items)

    def __initData(self):
        # vc = VehiclePark.maxAmount
        types = VehiclePark.types
        #TODO вставить распределение из скрипта distribution.py
        aid = self.inputData.algorithmId
        startAgeOfList = 0
        if aid == 0:
            startAgeOfList = 0
        elif aid == 1:
            startAgeOfList = 11
        elif aid == 2:
            startAgeOfList = 21
        for count in self.inputData.listAges:
            for _ in range(count):
                self.park.addVehicle(type=types[rd(0,1)], age=startAgeOfList)
            startAgeOfList += 1
        
    # def BreakOrNotAnyVehicle(self):
    #     for vehicle in self.park.park:
    #         chance = random.random() * vehicle.age
    #         if chance >= 10:
    #             vehicle.Break()

    # def ObsoleteOrNotAnyVehicle(self):
    #     for vehicle in self.park.park:
    #         if (vehicle.age >= self.inputData.obsoleteAge):
    #             chance = random.random() * vehicle.age
    #             if chance >= self.inputData.obsoleteAge:
    #                 vehicle.Obsolete()

    def BreakOrAndObsoleteAnyVehicle(self):
        age = 0
        obsAge = self.inputData.obsoleteAge
        for vehicle in self.park.park:
            age = vehicle.age

            chance = random.random() * age
            if chance >= 6:
                vehicle.Break()

            chance = random.random() * age
            if chance >= obsAge:
                vehicle.Obsolete()

    def getValue(self, verbsListFor10Years):
        #Kosn, Kisp, Ksov - коэф-ты временно упрощены и обобщены для упрощения задачи
        scale = 4
        penalty = 0.0
        Kosn = 0.0
        Kisp = 0.0
        Ksov = 0.0
        AbstractEff = 0.0
        # for i in range(int(len(verbsListFor10Years) / scale)):
        for i in range(10):
            verb1 = verbsListFor10Years[i*scale + 0]    #чинить рхм 6
            verb2 = verbsListFor10Years[i*scale + 1]    #купить рхм 6
            verb3 = verbsListFor10Years[i*scale + 2]    #чинить рхм 8
            verb4 = verbsListFor10Years[i*scale + 3]    #купить рхм 8

            penalty += self.park.sendToRepair(VehiclePark.types[0], verb1)
            penalty += self.park.buyNew(VehiclePark.types[0], verb2)

            penalty += self.park.sendToRepair(VehiclePark.types[1], verb3)
            penalty += self.park.buyNew(VehiclePark.types[1], verb4)

            Kosn += len(self.park) / self.inputData.parkCapacity
            try:
                Kisp += (len(self.park) - self.park.getBroken()) / len(self.park)
                Ksov += self.park.getModern() / len(self.park)
            except:
                Kisp = 0
                Ksov = 0
            #AbstractEff += self.park.getTotalEfficiency()

            self.park.passYear()
            self.BreakOrAndObsoleteAnyVehicle()

        # return Kosn + Kisp + Ksov + AbstractEff - penalty
        return Kosn + Kisp + Ksov - penalty
