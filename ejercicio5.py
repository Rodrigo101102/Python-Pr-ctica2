
from tabulate import tabulate

def ingresar_datos_estudiantes(cantidad_estudiantes):
    estudiantes = []
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

def ordenar_estudiantes(estudiantes):
    # Ordenar la lista de estudiantes por calificación de mayor a menor
    return sorted(estudiantes, key=lambda estudiante: estudiante[1], reverse=True)

def mostrar_tabla_estudiantes(estudiantes):
    tabla = []
    for estudiante in estudiantes:
        nombre, calificacion = estudiante
        estado = determinar_estado(calificacion)
        tabla.append([nombre, calificacion, estado])
    
    # Usamos tabulate para mostrar los datos en formato de tabla
    print(tabulate(tabla, headers=["Nombre", "Nota", "Estado"], tablefmt="grid"))

def programa_estudiantes():
    try:
        cantidad_estudiantes = int(input("¿Cuántos estudiantes hay en el curso? "))
        if cantidad_estudiantes <= 0:
            print("La cantidad de estudiantes debe ser mayor que 0.")
            return
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return
    
    estudiantes = ingresar_datos_estudiantes(cantidad_estudiantes)
    estudiantes_ordenados = ordenar_estudiantes(estudiantes)
    mostrar_tabla_estudiantes(estudiantes_ordenados)

# Ejecutar el programa
programa_estudiantes()
