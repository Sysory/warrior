class RHBZ_input():
  def __init__(self):
    self.parkCapacity : int = 0
    self.priceBuy : list[float] = [0]
    self.priceRep : list[float] = [0]
    self.moneyYear : float = 0
    self.moneyYearVol : float = 0
    self.obsoleteAge : int = 0

    self.populationSize : int = 0
    self.maxGenerations : int = 0
    self.pMutate : float = 0
    self.pCrossover : float  = 0

    self.v1 : int = 0
    self.v2 : int = 0
    self.v3 : int = 0
    self.Tc : int = 0
    self.listAges : list[int] = [0]
    self.algorithmId = 0;
