# Restaurante App

## Descripción

Este proyecto fue desarrollado en Python utilizando Programación Orientada a Objetos.

El programa permite registrar platillos y bebidas de un restaurante, almacenarlos en una lista, mostrar el menú disponible y buscar un producto por su nombre.

## Estructura del proyecto

- `main.py`: archivo principal que ejecuta el programa.
- `modelos/producto.py`: contiene la clase base `Producto`.
- `modelos/platillo.py`: contiene la clase `Platillo`, que hereda de `Producto`.
- `modelos/bebida.py`: contiene la clase `Bebida`, que hereda de `Producto`.
- `servicios/restaurante.py`: administra el menú del restaurante y la búsqueda de productos.

## Funciones principales

- Crear platillos y bebidas.
- Agregar productos al restaurante.
- Mostrar el menú del restaurante.
- Buscar un producto por su nombre.
- Mostrar la información del producto encontrado.

## Cómo ejecutar

1. Abrir el proyecto en Visual Studio Code.
2. Ejecutar el archivo `main.py`.
3. Escribir el nombre de un producto cuando el programa lo solicite.
4. El programa mostrará la información si el producto existe.

## Ejemplo

Al iniciar el programa se registran algunos platillos y bebidas de ejemplo. Después se muestra el menú del restaurante y el usuario puede escribir el nombre de un producto para buscarlo.

Si el producto existe, se muestra toda su información. Si no existe, el programa mostrará el mensaje:

**"Producto no existe."**
## Tecnologías utilizadas
- Python 3
- Programación Orientada a Objetos
- Git
- GitHub

## Autora
Josselyn Katerine Campoverde Encarnación
