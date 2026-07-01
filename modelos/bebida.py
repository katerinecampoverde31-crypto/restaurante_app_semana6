from modelos.producto import Producto

# Clase hija Bebida
class Bebida(Producto):

    def __init__(self, nombre, precio, disponible, volumen):
        super().__init__(nombre, precio, disponible)
        self.volumen = volumen

    # Muestra la información de la bebida
    def mostrar_informacion(self):
        print("------ Bebida ------")
        print("Nombre:", self.nombre)
        print("Precio: $", self.obtener_precio())
        print("Disponible:", self.disponible)
        print("Volumen:", self.volumen, "ml")