class Producto:

    #Clase que representa un producto en el inventario.


    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Inicializa un nuevo producto con los atributos dados.

        :param id_producto: ID único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad del producto en inventario.
        :param precio: Precio del producto.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        #Devuelve el ID del producto.
        return self.id_producto

    def establecer_id(self, id_producto):
        #Establece un nuevo ID para el producto.
        self.id_producto = id_producto

    def obtener_nombre(self):
        #Devuelve el nombre del producto.
        return self.nombre

    def establecer_nombre(self, nombre):
        #Establece un nuevo nombre para el producto.
        self.nombre = nombre

    def obtener_cantidad(self):
        #Devuelve la cantidad del producto en inventario.
        return self.cantidad

    def establecer_cantidad(self, cantidad):
        #Establece una nueva cantidad para el producto en inventario.
        self.cantidad = cantidad

    def obtener_precio(self):
        #Devuelve el precio del producto.
        return self.precio

    def establecer_precio(self, precio):
        #Establece un nuevo precio para el producto.
        self.precio = precio

    def __str__(self):
        #Devuelve una representación en cadena del producto.
        return f"ID: {self.id_producto}, NOMBRE: {self.nombre}, CANTIDAD: {self.cantidad}, PRECIO: ${self.precio:.2f}"
