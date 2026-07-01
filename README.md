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

## Herencia
La clase `Producto` es la clase base del sistema. Las clases `Platillo` y `Bebida` heredan de `Producto`, reutilizando sus atributos y métodos, además de incorporar características propias.

## Encapsulación

Se protegió el atributo `__precio` mediante encapsulación, permitiendo su acceso únicamente a través de los métodos definidos en la clase.

## Polimorfismo

El método `mostrar_informacion()` se implementó en las clases `Platillo` y `Bebida`, permitiendo que cada objeto muestre su información de acuerdo con su tipo.

## Reflexión

La Programación Orientada a Objetos permite desarrollar programas más organizados, reutilizables y fáciles de mantener. La aplicación de herencia, encapsulación y polimorfismo mejora la estructura y facilita futuras ampliaciones del sistema.
