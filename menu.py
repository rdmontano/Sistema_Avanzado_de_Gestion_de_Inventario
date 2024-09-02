import os
from inventario import Inventario
from producto import Producto

def limpiar_pantalla():
    #Limpia la pantalla de la consola según el sistema operativo.
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/MacOS
        os.system('clear')

def menu():

    #Muestra el menú interactivo para la gestión del inventario.

    inventario = Inventario()  # Carga el inventario automáticamente desde 'inventario.pkl o .txt' al iniciar

    while True:
        limpiar_pantalla()  # Limpia la pantalla antes de mostrar el menú

        print("\nSISTEMA DE GESTIÓN DE INVENTARIO")
        print("------------------------------------------")
        print("1. AÑADIR PRODUCTO")
        print("2. ELIMINAR PRODUCTO")
        print("3. ACTUALIZAR PRODUCTO")
        print("4. BUSCAR PRODUCTO POR NOMBRE")
        print("5. MOSTRAR TODOS LOS PRODUCTOS")
        print("6. GUARDAR INVENTARIO EN ARCHIVO")
        print("7. CARGAR INVENTARIO DESDE ARCHIVO")
        print("8. SALIR")

        print("\n------------------------------------------")
        opcion = input("SELECCIONE UNA OPCIÓN: ")

        limpiar_pantalla()  # Limpia la pantalla después de seleccionar una opción

        if opcion == '1':
            id_producto = input("INGRESE ID DEL PRODUCTO: ")
            nombre = input("INGRESE NOMBRE DEL PRODUCTO: ")
            cantidad = int(input("INGRESE CANTIDAD DEL PRODUCTO: "))
            precio = float(input("INGRESE PRECIO DEL PRODUCTO: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            print("------------------------------------------\n")
            inventario.añadir_producto(producto)
        elif opcion == '2':
            id_producto = input("INGRESE ID DEL PRODUCTO A ELIMINAR: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = input("INGRESE ID DEL PRODUCTO A ACTUALIZAR: ")
            nombre = input("INGRESE NUEVO NOMBRE (O PRESIONE ENTER PARA NO CAMBIAR): ")
            cantidad = input("INGRESE NUEVA CANTIDAD (O PRESIONE ENTER PARA NO CAMBIAR): ")
            precio = input("INGRESE NUEVO PRECIO (O PRESIONE ENTER PARA NO CAMBIAR): ")
            inventario.actualizar_producto(
                id_producto,
                nombre if nombre else None,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )
        elif opcion == '4':
            nombre = input("INGRESE EL NOMBRE DEL PRODUCTO A BUSCAR: ")
            print("------------------------------------------\n")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_productos()
        elif opcion == '6':
            inventario.guardar_en_archivo()
        elif opcion == '7':
            archivo = input("INGRESE EL NOMBRE DEL ARCHIVO PARA CARGAR EL INVENTARIO: ")
            inventario.archivo = archivo
            inventario.cargar_desde_archivo()
        elif opcion == '8':
            print("SALIENDO DEL SISTEMA...")
            break
        else:
            print("OPCION NO VALIDA. POR FAVOR, INTENTE DE NUEVO.")

        input("\nPRESIONE ENTER PARA CONTINUAR...")  # Pausa antes de regresar al menú


if __name__ == "__main__":
    menu()
