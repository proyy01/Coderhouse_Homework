class Cliente:
    def __init__(self, atributo1, atributo2, atributo3, atributo4):
        self.atributo1 = atributo1
        self.atributo2 = atributo2
        self.atributo3 = atributo3
        self.atributo4 = atributo4

        def metodo1(self): #Agregar Carrito
            pass

        def metodo2(self): #Pagar
            pass

        def __str__(self):
            return f"{self.atributo1}, {self.atributo2}, {self.atributo3}, {self.atributo4}"
