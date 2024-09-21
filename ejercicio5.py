from colorama import Fore, Style, init
from tabulate import tabulate

# Inicializar colorama
init(autoreset=True)

def ingresar_datos_estudiantes(estudiantes, cantidad_estudiantes):
    for i in range(1, cantidad_estudiantes + 1):
        nombre = input(f"Ingresa el nombre del estudiante {i}: ")
        
        # Ingreso de la primera nota
        while True:
            try:
                nota1 = float(input(f"Ingresa la primera nota de {nombre} (entre 0 y 20): "))
                if 0 <= nota1 <= 20:
                    break
                else:
                    print(Fore.RED + "La nota debe estar entre 0 y 20.")
            except ValueError:
                print(Fore.RED + "Por favor, ingresa un número válido para la primera nota.")
        
        # Ingreso de la segunda nota
        while True:
            try:
                nota2 = float(input(f"Ingresa la segunda nota de {nombre} (entre 0 y 20): "))
                if 0 <= nota2 <= 20:
                    break
                else:
                    print(Fore.RED + "La nota debe estar entre 0 y 20.")
            except ValueError:
                print(Fore.RED + "Por favor, ingresa un número válido para la segunda nota.")
        
        promedio = (nota1 + nota2) / 2
        estudiantes.append([nombre, nota1, nota2, promedio])
    
    return estudiantes

def determinar_estado(promedio):
    return "Aprobado" if promedio >= 10.5 else "Desaprobado"

def mostrar_tabla_estudiantes(estudiantes, con_indice=True):
    tabla = []
    for idx, estudiante in enumerate(estudiantes, start=1):
        nombre, nota1, nota2, promedio = estudiante
        estado = determinar_estado(promedio)
        color_estado = Fore.GREEN if estado == "Aprobado" else Fore.RED
        fila = [idx, nombre, nota1, nota2, promedio, f"{color_estado}{estado}{Style.RESET_ALL}"] if con_indice else [nombre, nota1, nota2, promedio, f"{color_estado}{estado}{Style.RESET_ALL}"]
        tabla.append(fila)

    headers = ["#", "Nombre", "Nota 1", "Nota 2", "Promedio", "Estado"] if con_indice else ["Nombre", "Nota 1", "Nota 2", "Promedio", "Estado"]
    print(tabulate(tabla, headers=headers, tablefmt="grid"))

def editar_estudiante(estudiantes):
    if estudiantes:
        while True:
            print("\nLista de estudiantes:")
            mostrar_tabla_estudiantes(estudiantes)  # Mostrar tabla con índice
            try:
                numero = int(input(Fore.CYAN + "Ingresa el número del estudiante que deseas editar o 0 para volver al menú: ")) - 1
                if numero == -1:
                    break  # Volver al menú
                elif 0 <= numero < len(estudiantes):
                    print(f"1. Nombre actual: {estudiantes[numero][0]}")
                    print(f"2. Nota 1 actual: {estudiantes[numero][1]}")
                    print(f"3. Nota 2 actual: {estudiantes[numero][2]}")
                    opcion_editar = input(Fore.CYAN + "¿Qué deseas editar? (1=Nombre, 2=Nota 1, 3=Nota 2, 0=Volver al menú): ")
                    if opcion_editar == "1":
                        nuevo_nombre = input("Ingresa el nuevo nombre: ")
                        estudiantes[numero][0] = nuevo_nombre
                    elif opcion_editar == "2":
                        nueva_nota1 = float(input("Ingresa la nueva Nota 1: "))
                        estudiantes[numero][1] = nueva_nota1
                    elif opcion_editar == "3":
                        nueva_nota2 = float(input("Ingresa la nueva Nota 2: "))
                        estudiantes[numero][2] = nueva_nota2
                    elif opcion_editar == "0":
                        break  # Volver al menú
                    else:
                        print(Fore.YELLOW + "Opción no válida. Intenta de nuevo.")
                    estudiantes[numero][3] = (estudiantes[numero][1] + estudiantes[numero][2]) / 2
                else:
                    print(Fore.YELLOW + "Número de estudiante no válido. Intenta de nuevo.")
            except ValueError:
                print(Fore.YELLOW + "Por favor, ingresa un número válido.")
    else:
        print(Fore.RED + "No hay estudiantes registrados.")

def borrar_estudiante(estudiantes):
    if estudiantes:
        while True:
            print("\nLista de estudiantes:")
            mostrar_tabla_estudiantes(estudiantes)  # Mostrar tabla con índice
            try:
                numero = int(input(Fore.CYAN + "Ingresa el número del estudiante que deseas borrar o 0 para volver al menú: ")) - 1
                if numero == -1:
                    break  # Volver al menú
                elif 0 <= numero < len(estudiantes):
                    estudiantes.pop(numero)
                    print(Fore.GREEN + "Estudiante eliminado.")
                else:
                    print(Fore.YELLOW + "Número de estudiante no válido. Intenta de nuevo.")
            except ValueError:
                print(Fore.YELLOW + "Por favor, ingresa un número válido.")
    else:
        print(Fore.RED + "No hay estudiantes registrados.")

def mostrar_estudiantes_ordenados(estudiantes):
    if estudiantes:
        estudiantes_ordenados = sorted(estudiantes, key=lambda x: x[3], reverse=True)
        mostrar_tabla_estudiantes(estudiantes_ordenados, con_indice=False)  # Mostrar tabla sin índice
    else:
        print(Fore.RED + "No hay estudiantes registrados.")

def programa_estudiantes():
    estudiantes = []

    while True:
        print(Fore.BLUE + "\nMenú:")
        print(Fore.CYAN + "1. Ingresar estudiantes")
        print(Fore.CYAN + "2. Editar estudiante")
        print(Fore.CYAN + "3. Borrar estudiante")
        print(Fore.CYAN + "4. Mostrar estudiantes ordenados por promedio")
        print(Fore.CYAN + "5. Salir")

        opcion = input(Fore.CYAN + "Selecciona una opción: ")

        if opcion == "1":
            try:
                cantidad_estudiantes = int(input("¿Cuántos estudiantes deseas agregar? "))
                if cantidad_estudiantes <= 0:
                    print(Fore.YELLOW + "La cantidad de estudiantes debe ser mayor que 0.")
                    continue
            except ValueError:
                print(Fore.YELLOW + "Por favor, ingresa un número válido.")
                continue
            
            estudiantes = ingresar_datos_estudiantes(estudiantes, cantidad_estudiantes)
            mostrar_tabla_estudiantes(estudiantes)

        elif opcion == "2":
            editar_estudiante(estudiantes)

        elif opcion == "3":
            borrar_estudiante(estudiantes)

        elif opcion == "4":
            print("\n" + Fore.WHITE + "Estudiantes ordenados por promedio:")
            mostrar_estudiantes_ordenados(estudiantes)

        elif opcion == "5":
            print(Fore.GREEN + "Saliendo del programa.")
            break

        else:
            print(Fore.YELLOW + "Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el programa
programa_estudiantes()
