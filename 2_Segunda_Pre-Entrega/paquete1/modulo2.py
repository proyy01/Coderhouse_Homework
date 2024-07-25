class Cliente:
    def __init__(self, nombre, contraseña, dirección, lista_de_compras):
        self.nombre = nombre
        self.__contraseña = contraseña
        self.dirección = dirección
        self.lista_de_compras = lista_de_compras

        def agregar(self): #Agregar Carrito
            print("Se ha agregado el artículo al carrito de compras.")

        def pagar(self): #Pagar
            print("Se han pagado los artículos dentro del carrito de compras.")

        def __str__(self):
            return f"{self.nombre}, {self.__contraseña}, {self.dirección}, {self.lista_de_compras}"
