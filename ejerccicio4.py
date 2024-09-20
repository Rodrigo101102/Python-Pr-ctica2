
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades 
# y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ 
# y si es mayor de 18 años, 10€. (10p)

#UTILIZAREMOS COSTANTES PARA LOS LÍMITES DE LA EDAD Y PRECIOS
#ESTO NOS AYUDARA A MODIFICAR FACILMENTE LOS VALORES POR SI LAS REGLAS DEL JUEGO CAMBIAN

EDAD_MINIMA_PAGO = 4
EDAD_CAMBIO_TARIFA = 18
TARIFA_JOVEN = 5
TARIFA_ADULTO = 10

#REALIZAREMOS UN FUNCIÓN PARA CALCULAR EL PRECIO

def calcular_precio_entrada(edad):
    if edad < EDAD_MINIMA_PAGO:
        return 0
    elif edad <= EDAD_CAMBIO_TARIFA:
        return TARIFA_JOVEN
    else:
        return TARIFA_ADULTO
#DEFINIMOS LA FUNCION MAIN QUE NOS AYUDARA A AGRUPAR LA LOGICA PRINCIPAL, ESTO NOS AYUDARA
#EVITAR CONTAMINAR EL ESPACION DE NOMBRES GLOBALES
#NOS PERMITE TAMBIEN TENER UN MEJOR CONTROL SOBRE CUANDO SE EJECUTARA LA LOGICA PRINCIPAL

def main():
    while True:
        try:
            edad = int(input('Por favor ingrese su edad: '))
            if edad < 0:
                print('La edad no puedes ser negativa. Intente de nuevo.')
                continue
            
            precio = calcular_precio_entrada(edad)
            
            if precio == 0:
                print(f'Para la edad de {edad} años, la entrada es gratis.')
            else:
                print(f'Para la edad de {edad} años, el costo de su entrada es de: {precio}€')
            break
        except ValueError:
            print('Por favor ingresar un dato numérico válido (por ejemplo: 10, 16, 20 ...)')

if __name__ == "__main__":
    main()