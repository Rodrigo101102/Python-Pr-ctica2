# Almacenar la contraseña en una variable
password_guardada= "JuanNeira2024"
password_ingresada = input("Favor introduce la contraseña: ")
if password_ingresada.lower() == password_guardada.lower():
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")