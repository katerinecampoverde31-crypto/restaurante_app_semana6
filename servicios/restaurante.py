from modelos.platillo import Platillo
from modelos.bebida import Bebida

class Restaurante:

    def __init__(self):
        self.lista_productos = []

    def agregar(self, producto):
        self.lista_productos.append(producto)

    def mostrar_menu(self):
        print("\nMENU DEL RESTAURANTE")

        if len(self.lista_productos) == 0:
            print("No hay productos.")
            return

        for producto in self.lista_productos:
            producto.mostrar_informacion()
            print()

    def buscar(self, nombre):
        for producto in self.lista_productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None


restaurante = Restaurante()

p1 = Platillo("Arroz con pollo", 5.50, True, 700)
p2 = Platillo("Seco de carne", 6.75, True, 850)

b1 = Bebida("Cola", 1.25, True, 500)
b2 = Bebida("Jugo", 2.00, False, 300)

restaurante.agregar(p1)
restaurante.agregar(p2)
restaurante.agregar(b1)
restaurante.agregar(b2)

restaurante.mostrar_menu()

print("Buscando producto...")

encontrado = restaurante.buscar("Cola")

if encontrado:
    print("Producto encontrado")
    encontrado.mostrar_informacion()
else:
    print("Producto no existe")