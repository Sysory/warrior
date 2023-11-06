from matplotlib import pyplot as plt
from InputData import InputData

class Chart:
    def __init__(self,
                 x : list[int] = 0,
                 y : list[int] = 0,
                 data : InputData = None):
        self.x : list[int] = x
        self.y : list[int] = y
        self.data = data
    
    def initData(self, y : list[int], tc : int = 0):
        self.y = y
        self.tc = tc
    
    def DrawChart(self):
        plt.plot(self.x, self.y)
        plt.show()

class Chart1to10(Chart):
    def __init__(self, y : list[int]):
        self.x : list[int] = [x for x in range(1, 11)]

class Chart11to20(Chart):
    def __init__(self, y : list[int]):
        self.x : list[int] = [x for x in range(11, 21)]

class ChartOver20(Chart):
    def __init__(self, y : list[int], data : InputData):
        self.x : list[int] = [x for x in range(21, data.getTc() + 1)]