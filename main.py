from servicios.restaurante import Restaurante
from modelos.platillo import Platillo
from modelos.bebida import Bebida

# Crear el restaurante
restaurante = Restaurante()

# Crear platillos
p1 = Platillo("Arroz con pollo", 5.50, True, 700)
p2 = Platillo("Seco de carne", 6.75, True, 850)

# Crear bebidas
b1 = Bebida("Cola", 1.25, True, 500)
b2 = Bebida("Jugo", 2.00, False, 300)

# Agregar productos
restaurante.agregar(p1)
restaurante.agregar(p2)
restaurante.agregar(b1)
restaurante.agregar(b2)

# Mostrar el menú
print("MENU DEL RESTAURANTE")
restaurante.mostrar_menu()

# Buscar un producto
nombre = input("\nIngrese el nombre del producto: ")

producto = restaurante.buscar(nombre)

if producto:
    print("\nProducto encontrado")
    producto.mostrar_informacion()
else:
    print("\nProducto no existe.")