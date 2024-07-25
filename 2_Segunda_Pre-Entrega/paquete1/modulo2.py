class Cliente:
    def __init__(self, nombre, fecha_de_nacimiento, dirección, teléfono):
        self.nombre = nombre
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.dirección = dirección
        self.teléfono = teléfono
    
        def agregar(self): #Agregar Carrito
            artículo = input("Indique el producto que desee agregar:")
            print(f"Se ha agregado {artículo} al carrito de compras.")

        def pagar(self): #Pagar
            print("Se han pagado los artículos dentro del carrito de compras.")

        def __str__(self):
            return f"Nombre:{self.nombre}, Fecha de nacimiento:{self.fecha_de_nacimiento}, Dirección:{self.dirección}, Teléfono:{self.teléfono}"
        
cliente = Cliente("Lord Baldomero", "Escuela Taradowarts", "+56 9 1234 5678", "Cartas de magia")