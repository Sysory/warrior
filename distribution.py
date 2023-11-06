from math import ceil
from RHBZ_input import RHBZ_input

def moduleSumForNegative(ntList):
    return len([nt for nt in ntList if nt < 0])

def countNegative(ntList):
    isNegative = lambda x: x < 0
    return len(list(filter(isNegative, ntList)))

def _1to10(data : RHBZ_input) -> list[int]:
    v1 = data.v1
    v2 = data.v2
    
    formula = lambda t: t * (v2 - v1)/55 + v1/5 - v2/10 
    ntList = [formula(t) for t in range(1, 11)]

    if (v1 < v2/2):
        s = moduleSumForNegative(ntList)
        nextNonNegative = countNegative(ntList)

        rule = lambda x: max(0, x)  #возвращает ноль, если число отрицательное. иначе возвращает свой аргумент
        ntList = list(map(rule, ntList))    #применяет функцию к списку
        cur = nextNonNegative

        while (cur < len(ntList)):
            if (s <= ntList[cur]):
                ntList[cur] -= s
                s = 0
                break
            else:
                s -= ntList[cur]
                ntList[cur] = 0
            
            cur += 1
    # return ntList
    return list(map(round, ntList))

def _11to20(data : RHBZ_input) -> list[int]:
    v2 = data.v2

    nt = v2/10
    ntList = [nt] * 10
    for i in range(ceil((nt - int(nt)) * 10)):
        ntList[i] = ntList[i] + 1
    ntList = list(map(int, ntList))
    # return ntList
    return list(map(round, ntList))

def _over20(data : RHBZ_input) -> list[int]:
    v2 = data.v2
    v3 = data.v3
    Tc = data.Tc
    
    formula = lambda t: 2*v3/(Tc-20) - v2/10 + (Tc-t+1)*( (v2/5 - (2*v3)/(Tc-20) )/(Tc-19) )
    ntList = [formula(t) for t in range(21, Tc+1)]

    if (v3/(Tc - 20) < v2/20):
        s = moduleSumForNegative(ntList)
        nextNonNegative = len(ntList) - 1 - countNegative(ntList)

        rule = lambda x: max(0, x)
        ntList = list(map(rule, ntList))
        cur = nextNonNegative

        while (cur > 0):
            if (s <= ntList[cur]):
                ntList[cur] -= s
                s = 0
                break
            else:
                s -= ntList[cur]
                ntList[cur] = 0
            cur -= 1
    # return ntList
    return list(map(round, ntList))

def main():
    def getInt(msg = ""):
        intNum = 0
        while (True):
            try:  intNum = int(input(msg))
            except: print("bad value")
            else: break
        return intNum   

    choiseMsg = "0: exit\n1: 1-10\n2: 11-20\n3: 21-Tc\n= "
    choise = -1
    while (choise not in (0, 1, 2, 3)):
        choise = getInt(choiseMsg)
    data = RHBZ_input()
    if (choise == 0):
        exit()

    elif (choise == 1):
        data.v1 = getInt("v1 = ")
        data.v2 = getInt("v2 = ")
        print(_1to10(data))

    elif (choise == 2):
        data.v2 = getInt("v2 = ")
        print(_11to20(data))

    elif (choise == 3):
        data.v2 = getInt("v2 = ")
        data.v3 = getInt("v3 = ")
        data.Tc = getInt("Tc = ")
        print(_over20(data))

if __name__ == "__main__":
    while (True): main()
