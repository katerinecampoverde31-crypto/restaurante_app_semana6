from modelos.producto import Producto

# Clase hija Platillo
class Platillo(Producto):

    def __init__(self, nombre, precio, disponible, calorias):
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias

    # Muestra la información del platillo
    def mostrar_informacion(self):
        print("----- Platillo -----")
        print("Nombre:", self.nombre)
        print("Precio: $", self.obtener_precio())
        print("Disponible:", self.disponible)
        print("Calorías:", self.calorias)