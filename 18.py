#18) Juguemos al juego de adivinar el numero, generaremos un número entre 1 y 100.
#Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor que el número buscado. 
# También poner el número de intentos requeridos.
import random
numeroA=random.randrange(1,100)
intentos=int(input("Digite numero de intentos: "))
i=1
bandera=True
while i<=intentos and bandera==True:
    numero=int(input("Adivine el numero. Digite numero: "))
    if(numero==numeroA):
        print("Ganaste :)")
        bandera=False
    else:
        if(numeroA<numero):
            print("el numero es menor a "+str(numero))
        else:
            print("el numero es mayor a "+str(numero))
    i+=1
i+1
if(i>intentos):
    print("Perdiste :(")