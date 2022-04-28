import csv
from registro import registro
class manejador:
    __lista=[]
    def __init__(self):
        for i in range (30):
            self.__lista.append([])
            for j in range (24):
                self.__lista[i].append(None)
    def __str__(self):
        return "%s"%(self.__lista)
    def Cargar(self):
        archivo=open('datos.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            nuevo=registro(float(fila[2].replace(',','.')),float(fila[3].replace(',','.')),float(fila[4].replace(',','.')))
            self.__lista[int(fila[0])-1][int(fila[1])]=nuevo
        archivo.close()
        return
    def menor(self):

        menor_t=9999
        menor_h=9999
        menor_p=9999
        for i in range(30):
            for j in range (24):
                if self.__lista[i][j].gettemp()< menor_t:
                    menor_t=self.__lista[i][j].gettemp()
                    diat=i+1
                    horat=j
                if self.__lista[i][j].gethum()< menor_h:
                    menor_h=self.__lista[i][j].gethum()
                    diah=i+1
                    horah=j
                if self.__lista[i][j].getpres()< menor_p:
                    menor_p=self.__lista[i][j].getpres()
                    diap=i+1
                    horap=j
        print("la temperatura mas baja fue el dia {} a la hora {}".format(diat,horat))
        print("la humedad mas baja fue el dia {} a la hora{}".format(diah,horah))
        print("la presion mas baja fue el dia {} a la hora {}".format(diap,horap))
        return
    def mayor(self):
        mayor_t=-9999
        mayor_h=0
        mayor_p=0
        for i in range(30):
            for j in range (24):
                if self.__lista[i][j].gettemp()> mayor_t:
                    mayor_t=self.__lista[i][j].gettemp()
                    diat=i+1
                    horat=j
                if self.__lista[i][j].gethum()> mayor_h:
                    mayor_h=self.__lista[i][j].gethum()
                    diah=i+1
                    horah=j
                if self.__lista[i][j].getpres()> mayor_p:
                    mayor_p=self.__lista[i][j].getpres()
                    diap=i+1
                    horap=j
        print("la temperatura mas alta fue el dia {} a la hora {}".format(diat,horat))
        print("la humedad mas alta fue el dia {} a la hora{}".format(diah,horah))
        print("la presion mas alta fue el dia {} a la hora {}".format(diap,horap))
        return
    def prom(self):
        acum=0
        for i in range(30):
            for j in range(24):
                acum+=self.__lista[i][j].gettemp()
        promedio=acum/30
        return promedio
        
    def listado(self,dia):
        dia=dia-1
        print("Hora    Temperatura    Humedad    Presion")
        for i in range (24):
            print(str(i).ljust(7),str(self.__lista[dia][i].gettemp()).ljust(14),str(self.__lista[dia][i].gethum()).ljust(11),str(self.__lista[dia][i].getpres()).ljust(7))



       