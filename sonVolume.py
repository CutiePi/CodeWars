class Enceinte:
    pSeuil = 2.3
    vSeuil = 7.41

    def __init__(self, pressure,volume):
        self.pressure = pressure
        self.volume = volume

    def getVolume(self):
        return self.volume
    def getPressure(self):
        return self.pressure

    def checkState(self):
        cPressure = self.pressure
        cVolume = self.volume
        if(cPressure>self.pSeuil and cVolume>self.vSeuil):
            print("stop")
        elif(cPressure>self.pSeuil):
            print("raise volume")
        elif(cVolume>self.vSeuil):
            print("lower volume")
        else:
            print("everything is fine")


#e  = Enceinte(2.3,7.4)
#e.checkState()
#print(e.getVolume())
#print(e.getPressure())