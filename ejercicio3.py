def obtener_renta():
    while True:
        try:
            renta = float(
                input("Por favor, ingrese su renta anual en euros: "))
            if renta < 0:
                raise ValueError(
                    "La renta no puede ser negativa. Intente de nuevo.")
            return renta
        except ValueError as e:
            print(f"Error: {e}. Asegúrese de ingresar un número válido.")


def calcular_tipo_impositivo(renta):
    if renta < 10000:
        return "5%"
    elif 10000 <= renta < 20000:
        return "15%"
    elif 20000 <= renta < 35000:
        return "20%"
    elif 35000 <= renta <= 60000:
        return "30%"
    else:
        return "45%"


def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Calcular tipo impositivo")
    print("2. Salir")


def calcular_tipo_impositivo_principal():
    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción (1 o 2): "))
            if opcion == 1:
                renta = obtener_renta()
                tipo_impositivo = calcular_tipo_impositivo(renta)
                print(f"El tipo impositivo que le corresponde es: {tipo_impositivo}")
            elif opcion == 2:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, elija 1 o 2.")

        except ValueError:
            print("Error: Debe ingresar un número entero (1 o 2).")


calcular_tipo_impositivo_principal()
