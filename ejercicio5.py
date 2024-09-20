def mostrar_menu():
    print("\n--- Menú de Operaciones Matemáticas ---")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Salir")

def obtener_numeros():
    while True:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            return num1, num2
        except ValueError:
            print("Por favor, ingresa un número válido.")

def ejecutar_opcion(opcion):
    if opcion == 1:
        num1, num2 = obtener_numeros()
        print(f"El resultado de la suma es: {num1 + num2}")
    elif opcion == 2:
        num1, num2 = obtener_numeros()
        print(f"El resultado de la resta es: {num1 - num2}")
    elif opcion == 3:
        num1, num2 = obtener_numeros()
        print(f"El resultado de la multiplicación es: {num1 * num2}")
    elif opcion == 4:
        num1, num2 = obtener_numeros()
        if num2 == 0:
            print("No se puede dividir entre cero.")
        else:
            print(f"El resultado de la división es: {num1 / num2}")
    elif opcion == 5:
        print("Saliendo del programa. ¡Hasta luego!")
    else:
        print("Opción no válida, por favor selecciona una opción del menú.")

def programa_menu():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción (1-5): "))
            if opcion == 5:
                ejecutar_opcion(opcion)
                break
            ejecutar_opcion(opcion)
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Ejecutar el programa
programa_menu()
