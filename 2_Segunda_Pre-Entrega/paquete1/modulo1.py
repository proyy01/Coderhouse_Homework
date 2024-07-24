#Este es el script de la primera pre-entrega.

base_datos = {} #Aquí se guardarán los nombres de usuarios y contraseñas

def crear_usuario():
    #Esta función creará un usuario, es decir, nombre de usuario y contraseña. También las agregará a la base de datos.
    while True:
        nombre = input("Ingrese su nombre de usuario: ")
        if nombre in base_datos:
            print("Este nombre ya se encuentra registrado, intente de nuevo.")
            continue
        if not nombre:
            print("No se puede registrar un nombre de usuario vacío, intente de nuevo.")
        else:
            break
    while True:
        contraseña = input("Ingrese su contraseña: ")
        if not contraseña:
            print("No se puede registrar una contraseña vacía, intente de nuevo.")
        else:
            base_datos[nombre] = contraseña
            print("Usuario ha sido registrado con éxito.")
            break

def iniciar_sesion():
    #Esta función verifica que nombre de usuario y contraseña se encuentren en la base de datos, si es así, se iniciará sesión.
    nombre = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if nombre in base_datos and base_datos[nombre] == contraseña:
        print("Se ha iniciado sesión correctamente.")
    else:
        print("El nombre de usuario y contraseña no coinciden.")

def mostrar_usuarios():
    #Esta función muestra a los usuarios y contraseñas en una lista, también hace saber si la base de datos se encuentra vacía.
    if len(base_datos) > 0:
        for usuario , contraseña in base_datos.items():
            print(f"{usuario} : {contraseña}")
    else:
        print("No hay usuarios registrados.")

def menu():
    #Esta función abre el menú, el cual ofrece las opciones que el usuario necesite.
    while True:
        print("1. Crear usuario")
        print("2. Iniciar sesión")
        print("3. Mostrar usuarios")
        print("4. Salir")
        try:
            opción = int((input("Escoga la opción: ")))
        except:
            print("No has seleccionado una opción, intente de nuevo.")
            continue
        if opción == 1:
            crear_usuario()
        elif opción == 2:
            iniciar_sesion()
        elif opción == 3:
            mostrar_usuarios()
        elif opción == 4:
            print("Hasta la vista, baby...")
            break
        else:
            print("No has seleccionado una opción, intente de nuevo.")

menu()