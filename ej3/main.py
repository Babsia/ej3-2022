from manejado import manejador
from menu import menuu

if __name__=='__main__':
    bandera = False
    m=menuu()
    while not bandera:
        print("")
        print("a minimo y maximo para temperatura,humedad y presion")
        print("b temperatura mensual ")
        print("c Listar temperatura,humedad y presion ingresando un dia ")
        print("d salir")
        opcion= input("Ingrese una opción: ")
        m.opcion(opcion)
        bandera =(opcion)=='d'

