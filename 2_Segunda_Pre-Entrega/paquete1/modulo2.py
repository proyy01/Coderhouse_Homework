class Cliente:
    def __init__(self, nombre, fecha_de_nacimiento, direccion, telefono):
        self.nombre = nombre
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.direccion = direccion
        self.telefono = telefono
    
    def agregar(self, articulo): #Agregar Carrito
            return f"Se ha agregado {articulo} al carrito de compras."

    def pagar(self): #Pagar
            return "Se han pagado los artículos dentro del carrito de compras."

    def __str__(self):
            return (f"Nombre: {self.nombre}\n"
                    f"Fecha de Nacimiento: {self.fecha_de_nacimiento}\n"
                    f"Dirección: {self.direccion}\n"
                    f"Teléfono: {self.telefono}")
    
mi_cliente = Cliente("Lord Baldomero", "2 de Agosto de 1992", "Escuela Taratowarts", 9543123)