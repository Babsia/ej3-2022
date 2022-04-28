from manejado import manejador
class menuu:
    __switcher=None
    __M=None

    def __init__(self):
        self.__switcher = { 
            'a':self.opcion1,
            'b':self.opcion2,
            'c':self.opcion3,
            'd':self.salir,
            }
        self.__M=manejador()
        self.__M.Cargar()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')

    def opcion1(self):
        print("opcion a")
        self.__M.menor()
        self.__M.mayor()
        
    def opcion2(self):
        print("opcion b")
        print("el promedio es {}".format(self.__M.prom()))
        
    def opcion3(self):
        dia=int(input("ingrese el dia: "))
        self.__M.listado(dia)
        print("C")
        
