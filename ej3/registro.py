class registro:
    __temp=0
    __humedad=0
    __presion=0
    def __init__(self,temp,hum,pres):
        self.__humedad=hum
        self.__presion=pres
        self.__temp=temp
        return
    def gettemp(self):
        return self.__temp
    def gethum(self):
        return self.__humedad
    def getpres(self):
        return self.__presion
    
    


