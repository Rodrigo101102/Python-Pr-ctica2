# Almacenar la contraseña en una variable

password_guardada= "JuanNeira2024"
intentos = 0
max_intentos = 5
while intentos < max_intentos:
    password_ingresada = input("Favor introduce la contraseña: ")
    
    if password_ingresada.lower() == password_guardada.lower():
        print("La contraseña es correcta.")
        break
    else:
        intentos +=1
        print("La contraseña es incorrecta.")
    
if intentos == max_intentos:
    print("Has alcanzado el número máximo de intentos. Salida del programa.")
    