#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
#ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al 
#usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que 
#tributar o no. (10p)
try:
   usuario = int(input("ingre su edad :"))

   ingresos_mensuales = float(input("ingrese sus ingresos mensuales : "))

   if usuario > 16 and  ingresos_mensuales >= 1000 :
            print(" ingresas felicidaes   ")
   else:
         if usuario <= 16:
            print (" no puedes tributar , tienes que ser mayor de 16 años  ")
         elif ingresos_mensuales > 1000:
            print (" no puedes tributar , tus ingresos son menores a 1000")
except ValueError:
      print (" po favor , introduce un valor numerico valido ")