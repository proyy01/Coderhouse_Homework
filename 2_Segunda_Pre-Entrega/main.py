#Importar módulos
from paquete1.modulo1 import *
from paquete1.modulo2 import Cliente

#Instanciar objeto
mi_cliente = Cliente("Lord Baldomero", "2 de Agosto de 1992", "Escuela Taratowarts", 9543123)

#Darle acciones al objeto (Estos son solo ejemplos)
# mi_cliente.agregar("Cartas Magicas")
# mi_cliente.pagar()
# print(mi_cliente)

#Menú
def menu():
    #Esta función abre el menú, el cual ofrece las opciones que el usuario necesite.
    while True:
        print("1. Agregar artículo al carrito de compras")
        print("2. Pagar carrito de compras")
        print("3. Mostrar detalles del cliente")
        print("4. Salir")
        try:
            opción = int((input("Escoga la opción: ")))
        except:
            print("No has seleccionado una opción, intente de nuevo.")
            continue
        if opción == 1:
            articulo = input("Indique el producto que desee agregar: ")
            print(mi_cliente.agregar(articulo))
        elif opción == 2:
            print(mi_cliente.pagar())
        elif opción == 3:
            print(mi_cliente)
        elif opción == 4:
            print("Hasta la vista, baby...")
            break
        else:
            print("No has seleccionado una opción, intente de nuevo.")

menu()