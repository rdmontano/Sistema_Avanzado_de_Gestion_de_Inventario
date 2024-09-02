import pickle
from producto import Producto


class Inventario:

    #Clase que representa el inventario de productos.

    def __init__(self, archivo='inventario.txt'):
        """
        Inicializa el inventario y carga los productos desde un archivo si existe.

        :param archivo: Nombre del archivo donde se guarda el inventario.
        """
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario.

        :param producto: Instancia de la clase Producto a añadir.
        """
        if producto.obtener_id() in self.productos:
            print(f"EL PRODUCTO CON ID {producto.obtener_id()} YA EXISTE.")
        else:
            self.productos[producto.obtener_id()] = producto
            print(f"PRODUCTO {producto.obtener_nombre()} AÑADIDO AL INVENTARIO.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID.

        :param id_producto: ID del producto a eliminar.
        """
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"PRODUCTO CON ID {id_producto} ELIMINADO DEL INVENTARIO.")
        else:
            print(f"PRODUCTO CON ID {id_producto} NO ENCONTRADO.")

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        """
        Actualiza los detalles de un producto en el inventario.

        :param id_producto: ID del producto a actualizar.
        :param nombre: Nuevo nombre del producto.
        :param cantidad: Nueva cantidad del producto.
        :param precio: Nuevo precio del producto.
        """
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nombre:
                producto.establecer_nombre(nombre)
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)
            print(f"PRODUCTO CON ID {id_producto} ACTUALIZADO.")
        else:
            print(f"PRODUCTO CON ID {id_producto} NO ENCONTRADO.")

    def buscar_producto(self, nombre):
        """
        Busca productos por nombre en el inventario.

        :param nombre: Nombre del producto a buscar.
        """
        encontrados = [producto for producto in self.productos.values() if
                       producto.obtener_nombre().lower() == nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print(f"NO SE ENCONTRARON PRODUCTOS CON EL NOMBRE '{nombre}'.")

    def mostrar_productos(self):
        #Muestra todos los productos en el inventario.
        if self.productos:
            print("\nINVENTARIO DE PRODUCTOS:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("NO HAY PRODUCTOS EN EL INVENTARIO.")

    def guardar_en_archivo(self):
        #Guarda el inventario actual en un archivo.
        with open(self.archivo, 'wb') as f:
            pickle.dump(self.productos, f)
        print(f"INVENTARIO GUARDADO EN {self.archivo}.")

    def cargar_desde_archivo(self):
        #Carga el inventario desde un archivo, si existe.
        try:
            with open(self.archivo, 'rb') as f:
                self.productos = pickle.load(f)
            print(f"INVENTARIO CARGADO DESDE {self.archivo}.")
        except FileNotFoundError:
            print(f"NO SE ENCONTRÓ EL ARCHIVO {self.archivo}. SE HA CREADO UN INVENTARIO NUEVO.")
        except EOFError:
            print("EL ARCHIVO ESTA VACIO. SE HA CREADO UN INVENTARIO NUEVO.")
        except Exception as e:
            print(f"OCURRIO UN ERROR AL CARGAR EL ARCHIVO: {e}")
            self.productos = {}
