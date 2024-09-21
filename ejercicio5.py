from colorama import Fore, Style
from tabulate import tabulate

def ingresar_datos_estudiantes(estudiantes, cantidad_estudiantes):
    for i in range(1, cantidad_estudiantes + 1):
        nombre = input(f"Ingresa el nombre del estudiante {i}: ")
        while True:
            try:
                calificacion = float(input(f"Ingresa la calificación de {nombre} (entre 0 y 20): "))
                if 0 <= calificacion <= 20:
                    estudiantes.append([nombre, calificacion])
                    break
                else:
                    print("La calificación debe estar entre 0 y 20.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
    return estudiantes

def determinar_estado(calificacion):
    return "Aprobado" if calificacion >= 10.5 else "Desaprobado"

def mostrar_tabla_estudiantes(estudiantes):
    tabla = []
    for idx, estudiante in enumerate(estudiantes, start=1):
        nombre, calificacion = estudiante
        estado = determinar_estado(calificacion)
        color_estado = Fore.GREEN if estado == "Aprobado" else Fore.RED
        tabla.append([idx, nombre, calificacion, f"{color_estado}{estado}{Style.RESET_ALL}"])
    
    print(tabulate(tabla, headers=["#", "Nombre", "Nota", "Estado"], tablefmt="grid"))

def editar_estudiante(estudiantes):
    mostrar_tabla_estudiantes(estudiantes)
    try:
        numero = int(input("Ingresa el número del estudiante cuya nota deseas editar: ")) - 1
        if 0 <= numero < len(estudiantes):
            while True:
                try:
                    nueva_calificacion = float(input(f"Ingresa la nueva calificación (actual: {estudiantes[numero][1]}): "))
                    if 0 <= nueva_calificacion <= 20:
                        estudiantes[numero][1] = nueva_calificacion  # Solo editar la nota
                        break
                    else:
                        print("La calificación debe estar entre 0 y 20.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")
        else:
            print("Número de estudiante no válido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def filtrar_estudiante(estudiantes):
    nombre_buscar = input("Ingresa el nombre del estudiante a buscar: ")
    filtrados = [estudiante for estudiante in estudiantes if estudiante[0].lower() == nombre_buscar.lower()]
    
    if filtrados:
        mostrar_tabla_estudiantes(filtrados)
    else:
        print("Estudiante no encontrado.")

def programa_estudiantes():
    estudiantes = []  # Lista vacía al inicio del programa

    while True:
        print("\nMenú:")
        print("1. Ingresar notas de estudiantes")
        print("2. Editar nota de un estudiante")
        print("3. Filtrar estudiante por nombre")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                cantidad_estudiantes = int(input("¿Cuántos estudiantes deseas agregar? "))
                if cantidad_estudiantes <= 0:
                    print("La cantidad de estudiantes debe ser mayor que 0.")
                    continue
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue
            
            estudiantes = ingresar_datos_estudiantes(estudiantes, cantidad_estudiantes)  # Agregar estudiantes a la lista
            mostrar_tabla_estudiantes(estudiantes)

        elif opcion == "2":
            if estudiantes:
                editar_estudiante(estudiantes)
                mostrar_tabla_estudiantes(estudiantes)
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "3":
            if estudiantes:
                filtrar_estudiante(estudiantes)
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el programa
programa_estudiantes()
