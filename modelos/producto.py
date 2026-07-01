# Clase Producto
class Producto:

    def __init__(self, nombre, precio, disponible):
        self.nombre = nombre
        self.__precio = precio
        self.disponible = disponible

    # Devuelve el precio del producto
    def obtener_precio(self):
        return self.__precio

    # Permite cambiar el precio
    def cambiar_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("No se puede ingresar un precio menor o igual a 0.")

    # Muestra la información del producto
    def mostrar_informacion(self):
        print("Nombre del producto:", self.nombre)
        print("Precio: $", self.__precio)
        print("Disponible:", self.disponible)